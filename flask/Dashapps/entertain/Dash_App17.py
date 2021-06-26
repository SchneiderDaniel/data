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

url_base = '/dash/app17/' 

data_sources = [
    "https://www.kaggle.com/prateekmaj21/disney-movies"
]

data_licenses = [
]

sourced_date = "05/17/2021"

cite_text = '"All our dreams can come true — if we have the courage to pursue them."'
cite_author = "Walt Disney"
cite_link = "https://en.wikipedia.org/wiki/Walt_Disney"
description_text = '''On this chart you see the Top 20 Disney Movies based on their gross return in dollar, which is adjusted by the inflation. For me the order was quite suprising. For you as well?'''
hint_text = ""
df = pd.read_csv('app_data/processed/0017.csv')
df = df.sort_values('inflation_adjusted_gross', ascending=False)
df = df.head(20)

fig = px.bar(df, y="movie_title", x="inflation_adjusted_gross", title="Top 20 Disney Movies with the highest gross return (inflation adjusted) ", labels={"movie_title": "Movie Title",  "inflation_adjusted_gross": "Gross Return (inf. adj.)"})
fig['layout']['yaxis']['autorange'] = "reversed"
fig.update_layout( legend=dict(
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
    height=800,
    margin={'r': 4,'l':10},yaxis={'visible': True})


# The Layout
layout = html.Div(style={'font-family':'"Poppins", sans-serif', 'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Gross Return of Disney Movies',
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
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    ),
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