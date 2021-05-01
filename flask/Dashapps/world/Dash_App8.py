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
from ..Dash_base import warning_card, colors, cite_card, description_card, draft_template
import dash_table
from datetime import datetime
import numpy as np
from flask import request
import locale


url_base = '/dash/app8/' 

data_sources = [
    "https://data.cdc.gov/NCHS/Weekly-Counts-of-Deaths-by-State-and-Select-Causes/3yf8-kanr",
    "https://data.cdc.gov/NCHS/Weekly-Counts-of-Deaths-by-State-and-Select-Causes/muzy-jte6",
    "https://www.reddit.com/r/dataisbeautiful/comments/mjdmln/oc_weekly_deaths_from_all_causes_by_year_in_the/"
]

data_licenses = [
    "https://www.usa.gov/government-works"
]

sourced_date = "03/20/2021"

cite_text = '"I will not say: do not weep; for not all tears are an evil."'
cite_author = "J.R.R. Tolkien"
cite_link = "https://en.wikipedia.org/wiki/J._R._R._Tolkien"
description_text = '''What you see below are the deaths in the USA in year 2020 in comparison to all the years before. We see how the pandamic affected the number of deaths per week in 2020.'''

df = pd.read_csv('app_data/processed/0008.csv', dtype={'Jurisdiction of Occurrence': str,'Year': int,'Week': int,'Cause': int})




chart_groups = df.groupby(by='Year')


chart_data = []

chart_colors=['orange', 'blue', 'green', 'black', 'grey', 'purple', 'red']


for group, dataframe in chart_groups:
    dataframe = dataframe.sort_values(by=['Week'])

    trace = go.Scatter(x=dataframe.Week.tolist(), 
                       y=dataframe.Cause.tolist(),
                       marker=dict(color=chart_colors[len(chart_data)]),
                       mode='lines+markers',
                       name=group)
    chart_data.append(trace)

chart_layout =  go.Layout(xaxis={'title': 'Week of the Year'},
                    yaxis={'title': 'Deaths per Week'},
                    margin={'l': 0, 'b': 50, 't': 50, 'r': 0},
                    legend = dict( 
                            orientation="h", # Looks much better horizontal than vertical
                            y=-0.15
                            ),
                            template=draft_template,
                            annotations=[
                                dict(
                                    templateitemname="draft watermark",
                                    text="www.blackandwhitedata.com",
                                )
                            ],                    
                    hovermode='closest')

fig = go.Figure(data=chart_data, layout=chart_layout)  


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