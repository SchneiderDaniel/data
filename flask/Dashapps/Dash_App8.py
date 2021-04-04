# -*- coding: utf-8 -*-

from dash import Dash
from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER, ClientsideFunction
from .Dash_fun import apply_layout_with_auth, load_object, save_object
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from .Dash_base import warning_card, colors
import dash_table
from datetime import datetime
import numpy as np
from flask import request
import locale


url_base = '/dash/app8/' 

df = pd.read_csv('app_data/processed/0008.csv', dtype={'Jurisdiction of Occurrence': str,'Year': int,'Week': int,'Cause': int})

chart_groups = df.groupby(by='Year')

print(chart_groups)

chart_data = []

chart_colors=['orange', 'blue', 'green', 'black', 'grey', 'purple', 'red']


for group, dataframe in chart_groups:
    dataframe = dataframe.sort_values(by=['Week'])
    print(dataframe)
    # print('______')
    # print(dataframe.Cause.tolist())

    trace = go.Scatter(x=dataframe.Week.tolist(), 
                       y=dataframe.Cause.tolist(),
                       marker=dict(color=chart_colors[len(chart_data)]),
                       mode='lines+markers',
                       name=group)
    chart_data.append(trace)

chart_layout =  go.Layout(xaxis={'title': 'Week of the Year'},
                    yaxis={'title': 'Deaths per Week'},
                    margin={'l': 40, 'b': 40, 't': 50, 'r': 50},
                    legend={'orientation': 'h'},
                    hovermode='closest')

fig = go.Figure(data=chart_data, layout=chart_layout)  


def description_card():
    return html.Div(
        id="description_card",
        children = [dcc.Markdown(''' What you see below are the deaths in the USA in year 2020 in comparison to all the years before. We see how the pandamic affected the number over deaths per week in 2020. ''')],
    style={
        'backgroundColor': colors['background'],
    })



# The Layout
layout = html.Div(style={'font-family':'"Poppins", sans-serif', 'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Deaths in the USA in 2020',
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
    html.Div(children=warning_card(), style={
        'textAlign': 'left',
        'color': colors['text'],
        'backgroundColor': colors['background']
    })
])

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base, external_stylesheets = [dbc.themes.BOOTSTRAP], external_scripts = ["https://cdn.plot.ly/plotly-locale-de-latest.js"], meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
    
    apply_layout_with_auth(app, layout)

    return app.server