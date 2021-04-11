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


url_base = '/dash/app5/' 

data_sources = [
    "https://www.kaggle.com/georgezakharov/historical-data-on-the-trading-of-cryptocurrencies"
]

data_licenses = [
    "https://creativecommons.org/publicdomain/zero/1.0/"
]


df = pd.read_csv('app_data/processed/0005.csv', dtype={'Year': int,'Name': str,'Color': str})


minYear = df['Year'].min()
maxYear = df['Year'].max()
marks_dict = {}
for i in range(minYear,maxYear+1):
    marks_dict[i]=str(i)




mask = (df['Year']==2016)
df_toDraw=df.loc[mask]
df_toDraw = df_toDraw.sort_values('Market Cap', ascending=True)
fig = go.Figure(go.Bar(
            x=df_toDraw['Market Cap'].tolist(),
            y=df_toDraw['Name'].tolist(),
            marker=dict(color=df_toDraw['Color']),
            orientation='h'))

fig.update_layout(
    height=800,
    margin=dict(
        l=50,
        r=0,
        b=100,
        t=100,
        pad=4
    )
)


def description_card():
    return html.Div(
        id="description_card",
        children = [dcc.Markdown(''' On this diagram you see the Top 20 Cryptocurrencies of the past few years. In these charts you will see the dominance of bitcoin. One says that this shows the irrelevance of all the other coins. And the others say that is shows the potential that is still hidden in these other coins. You choose your side ;)''')],
    style={
        'backgroundColor': colors['background'],
    })

# The Layout
layout = html.Div(style={'font-family':'"Poppins", sans-serif', 'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Top 20 Cryptocurrencies in $',
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
    html.Br(),
    html.Br(),
    dcc.Slider(
        id='ty-slider',
        min=minYear,
        max=maxYear,
        step=1,
        value=maxYear,
        updatemode='drag',
        marks = marks_dict,
        # tooltip = { 'always_visible': True },
    ),
    dcc.Graph(
        id='ty-figure',
        figure=fig
    ),
    
    html.Br(),
    html.Hr(className="my-2"),
    html.Br(),
    html.Div(children=warning_card(data_sources,data_licenses), style={
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


    @app.callback(
        [Output('ty-figure', 'figure'),
        Output('ty-figure', 'config')],
        Input('ty-slider', 'value')
    )
    def update_graph(value):
        # print(value)

        request_locale  = request.accept_languages.best_match(['en_US','de_DE'])
        if (request_locale=='en_US'): 
            dash_locale = 'en'
            sep_locale = "."
            request_locale_utf8 = 'en_US.utf8'
        else:
            dash_locale = 'de'
            sep_locale = ","
            request_locale_utf8 = 'de_DE.utf8'
        locale.setlocale(locale.LC_ALL, request_locale_utf8)

        # print(request_locale_utf8)

        mask = (df['Year']==value)
        df_toDraw=df.loc[mask]
        df_toDraw = df_toDraw.sort_values('Market Cap', ascending=True)
        fig_toDraw = go.Figure(go.Bar(
                    x=df_toDraw['Market Cap'].tolist(),
                    y=df_toDraw['Name'].tolist(),
                    marker=dict(color=df_toDraw['Color']),
                    orientation='h'))

        # fig_toDraw.update_traces(texttemplate='%{text:.2s}',textposition='outside',textfont_size=12)

        fig_toDraw.update_layout(
            height=800,
            margin=dict(
                l=50,
                r=0,
                b=100,
                t=100,
                pad=4
            )
        )

        fig_toDraw.update_xaxes(
            tickvals=[0,50000000000,100000000000,150000000000,200000000000],
            range=[0,200000000000]
        )

       

        return fig_toDraw,dict(locale=dash_locale)





        

    return app.server