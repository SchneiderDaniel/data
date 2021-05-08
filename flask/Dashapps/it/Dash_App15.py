# -*- coding: utf-8 -*-

from dash import Dash
from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER, ClientsideFunction
from Dashapps.Dash_fun import apply_layout_with_auth, load_object, save_object
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# https://github.com/plotly/dash-daq
#https://dash-docs.herokuapp.com/dash-daq
import dash_daq as daq
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from Dashapps.Dash_base import warning_card, colors, cite_card, description_card, hint_card
import dash_table
from datetime import datetime
import numpy as np
from flask import request
import locale

url_base = '/dash/app15/' 

data_sources = [
    "https://www.kaggle.com/ihelon/hello-world-in-programming-languages"
]

data_licenses = [
    "https://creativecommons.org/publicdomain/zero/1.0/"
]

sourced_date = "05/06/2021"

cite_text = '"Computer science inverts the normal. In normal science, you are given a world, and your job is to find out the rules. In computer science, you give the computer the rules, and it creates the world."'
cite_author = "Alan Kay"
cite_link = "https://en.wikipedia.org/wiki/Alan_Kay"
description_text = '''On this chart you see the most frequently used charaters in Hello World programs from over 600 languages. For each language a character only counts once. Moreover, we don't consider letters as well as numbers. Also breaks and empty spaces are discarded. '''
hint_text = ""
df = pd.read_csv('app_data/processed/0015.csv',)
fig = px.bar(df, x='Frequency', y='Character')

fig['layout']['yaxis']['autorange'] = "reversed"

fig.update_layout(
    showlegend=False,
    title_xanchor="auto",
    height=800,
    font=dict(
        size=16
    ),
    xaxis=dict(
        linecolor='black',
        showticklabels=True,
        showgrid=True,
        gridcolor='lightgray',
    ),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin_pad=5,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=20
    )
)

# The Layout
layout = html.Div(style={'font-family':'"Poppins", sans-serif', 'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Most Used Characters in Hello World Programs',
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
    #add fig here
    dcc.Graph(
        id='ty-figure',
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

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base, external_stylesheets = [dbc.themes.BOOTSTRAP], external_scripts = ["https://cdn.plot.ly/plotly-locale-de-latest.js"], meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
    
    apply_layout_with_auth(app, layout)

    return app.server