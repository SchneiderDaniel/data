# -*- coding: utf-8 -*-

from dash import Dash
from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER, ClientsideFunction
from Dashapps.Dash_fun import apply_layout_with_auth, load_object, save_object
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from Dashapps.Dash_base import warning_card, colors, cite_card, description_card, draft_template, hint_card
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

cite_text = '"You only live twice: Once when you are born and once when you look death in the face."'
cite_author = "Ian Fleming"
cite_link = "https://en.wikipedia.org/wiki/Ian_Fleming"
description_text = '''In this chart we take a look at the violence of James Bond movies. We define the violence of a movie by the sum of kills that were caused by James Bond himself and others. '''
hint_text = "With a click on the legend of the figure, your can select which type of kills you want to see."

df = pd.read_csv('app_data/processed/0006.csv', dtype={'Movie': str,'Kills by Bond': int,'Kills of Others': int})


# fig = px.bar(df, x="Movie", y=["Kills by Bond", "Kills of Others"], title="History of James Bond Movies",labels={'value':'Kills','variable':'Cause'})
fig = px.bar(df, y="Movie", x=["Kills by Bond", "Kills of Others"], title="History of James Bond Movies",labels={'value':'Kills','variable':'Cause'})
fig.update_layout(legend=dict(
    orientation="h",
  
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
),  
    annotations=[
        dict(
            textangle=-30,
            opacity=0.1,
            font=dict(color="black", size=35),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
            text="www.blackandwhitedata.com",
        )
    ],
    # template=draft_template,
    # annotations=[
    #     dict(
    #         templateitemname="draft watermark",
    #         text="www.blackandwhitedata.com",
    #     )
    # ],
    height=800,
    margin={'r': 4,'l':10},yaxis={'visible': True})


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
    html.Div(children=description_card(description_text), style={
        'textAlign': 'center',
        'color': colors['text'],
        'backgroundColor': colors['background']
    }),
    html.Div(children=cite_card(cite_text,cite_author,cite_link), style={
        'textAlign': 'center',
        'color': colors['text'],
        'backgroundColor': colors['background']
    }),
    html.Br(),
    html.Div(children=hint_card(hint_text), style={
        'textAlign': 'left',
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