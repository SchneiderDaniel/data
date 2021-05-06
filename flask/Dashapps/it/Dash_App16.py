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

url_base = '/dash/app16/' 

data_sources = [
    "https://www.kaggle.com/ihelon/hello-world-in-programming-languages"
]

data_licenses = [
    "https://creativecommons.org/publicdomain/zero/1.0/"
]

sourced_date = "05/06/2021"

cite_text = '"Computer science is not just for smart nerds in hoodies coding in basements. Coding is extremely creative and is an integral part of almost every industry."'
cite_author = "Reshma Saujani"
cite_link = "https://en.wikipedia.org/wiki/Reshma_Saujani"
description_text = '''On this chart you see the length of Hello World Programs in over 600 programming languages. Note, that a break and a space also contributes to the lenght with one.'''
hint_text = ""
df = pd.read_csv('app_data/processed/0016.csv')


# The Layout
layout = html.Div(style={'font-family':'"Poppins", sans-serif', 'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Length of Hello World Programs',
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