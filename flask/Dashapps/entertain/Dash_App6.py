# -*- coding: utf-8 -*-

from dash import Dash
from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER, ClientsideFunction
from ..Dash_fun import apply_layout_with_auth, load_object, save_object
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from ..Dash_base import warning_card, colors
import dash_table
from datetime import datetime
import numpy as np
from flask import request
import locale


url_base = '/dash/app6/' 

data_sources = [
    "https://www.kaggle.com/dreb87/jamesbond"
]

data_licenses = [
    "https://creativecommons.org/publicdomain/zero/1.0/"
]

sourced_date = "02/10/2021"

cite_text = ""
cite_author = ""

df = pd.read_csv('app_data/processed/0006.csv', dtype={'Movie': str,'Kills by Bond': int,'Kills of Others': int})



fig = px.bar(df, x="Movie", y=["Kills by Bond", "Kills of Others"], title="History of James Bond Movies",labels={'value':'Kills','variable':'Cause'})
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
),margin={'r': 1,'l':1},yaxis={'visible': True})

def description_card():
    return html.Div(
        id="description_card",
        children = [dcc.Markdown(''' In this chart we take a look at the violence of James Bond movies. We define the violence of a movie by the sum of kills that were caused by James Bond himself and others. '''),dbc.Alert("Info: By clicking on the legend you can switch the cause of the kills.", color="primary"),],
    style={
        'backgroundColor': colors['background'],
    })



# The Layout
layout = html.Div(style={'font-family':'"Poppins", sans-serif', 'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Violence in James Bond Movies',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'backgroundColor': colors['background']
        }
    ),
    html.Div(children=description_card(), style={
        'textAlign': 'center',
        'color': colors['text'],
        'backgroundColor': colors['background']
    }),
    
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    ),
    html.Br(),
    html.Hr(className="my-2"),
    html.Br(),
    html.Div(children=warning_card(data_sources,data_licenses,sourced_date), style={
        'textAlign': 'left',
        'color': colors['text'],
        'backgroundColor': colors['background']
    })
])

def cast_int(val):
    if val is None: return 1
    return int(val)

def cast_float(val):
    if val is None: return 1.0
    return float(val)

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base, external_stylesheets = [dbc.themes.BOOTSTRAP], external_scripts = ["https://cdn.plot.ly/plotly-locale-de-latest.js"], meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
    
    apply_layout_with_auth(app, layout)

    return app.server