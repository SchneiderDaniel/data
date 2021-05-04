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
from Dashapps.Dash_base import warning_card, colors, cite_card, cite_card, description_card, draft_template
import dash_table
from datetime import datetime
import numpy as np
from flask import request
import locale

url_base = '/dash/app7/' 

data_sources = [
    "https://www.kaggle.com/muhammadkhalid/most-popular-programming-languages-since-2004"
]

data_licenses = [
    "https://creativecommons.org/licenses/by/4.0/"
]

sourced_date = "04/28/2021"

cite_text = '"The most disastrous thing that you can ever learn is your first programming language."'
cite_author = "Alan Kay"
cite_link = "https://en.wikipedia.org/wiki/Alan_Kay"

description_text = '''On this pie chart you see the most popular programming languages in the past few years with the data pulled from github.'''

dateparse = lambda x: datetime.strptime(x, '%B %Y')

df = pd.read_csv('app_data/processed/0007.csv', parse_dates=['Date'], date_parser=dateparse)
df2 = pd.read_csv('app_data/processed/0007_2.csv', dtype={'Color': str})

minDate = 0
maxDate = len(df.index)
marks_dict = {}
date_list = df['Date'].tolist()
for i in range(len(date_list)):
    marks_dict[i]=str(date_list[i].strftime("%B %Y"))


#----
mask = (df['Date']==df['Date'].min())
df_toDraw=df.loc[mask].drop(['Date'], axis=1).transpose()
df_toDraw['Color'] = np.array(df2['Color'].tolist())

mask2 = (df_toDraw.iloc[:,0]!=0)
df_toDraw=df_toDraw.loc[mask2]
df_toDraw.rename(columns={ df_toDraw.columns[0]: "Percent" }, inplace=True)

df_toDraw['Name'] = df_toDraw.index

fig = go.Figure(data=[go.Pie(labels=df_toDraw['Name'].tolist(),
                             values=df_toDraw['Percent'].tolist())])

fig.update_traces(hoverinfo='label+percent', textposition='inside', textinfo='percent+label',  marker=dict(colors=df_toDraw['Color'].tolist(), line=dict(color='#000000', width=2)))

fig.update_layout(
    showlegend=False,
    title_xanchor="auto",
    height=800,
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
        children='Most Popular Programming Languages',
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
    html.P("Select:"),
    dcc.Slider(
        id='ty-slider',
        min=minDate,
        max=maxDate-1,
        # dots=False,
        step=1,
        value=minDate,
        # marks = marks_dict,
        # handleLabel={"showCurrentValue": True,"label": "VALUE"},
        updatemode='drag',
        # handleLabel=marks_dict
        # targets = marks_dict,
        # tooltip = { 'always_visible': False },
    ),
    html.Div(id="slider-value", style={"text-align": "right","font-style": "italic" }),
    html.Br(),
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
        Output("slider-value", "children"),
        ],
        [Input(component_id='ty-slider', component_property='value')]
    )
    def computeBalance(value_from_slider):

        # mask = (df['Date']==df['Date'].min())
        # df_toDraw=df.loc[mask].drop(['Date'], axis=1).transpose()
        df_toDraw = df.iloc[[value_from_slider]].drop(['Date'], axis=1).transpose()
        
        df_toDraw['Color'] = np.array(df2['Color'].tolist())

        mask2 = (df_toDraw.iloc[:,0]!=0)
        df_toDraw=df_toDraw.loc[mask2]
        df_toDraw.rename(columns={ df_toDraw.columns[0]: "Percent" }, inplace=True)

        df_toDraw['Name'] = df_toDraw.index

        fig_toDraw = go.Figure(data=[go.Pie(labels=df_toDraw['Name'].tolist(),
                                    values=df_toDraw['Percent'].tolist())])

        fig_toDraw.update_traces(hoverinfo='label+percent', textposition='inside', textinfo='percent+label',  marker=dict(colors=df_toDraw['Color'].tolist(), line=dict(color='#000000', width=2)))

        fig_toDraw.update_layout(
            showlegend=False,
            template=draft_template,
            annotations=[
                dict(
                    templateitemname="draft watermark",
                    text="www.blackandwhitedata.com",
                )
            ],
            title_xanchor="auto",
            height=800,
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=20
            )
        )

        return fig_toDraw,[str(marks_dict[value_from_slider])]


    # @app.callback(
    #     [Output('ty-figure', 'figure'),
    #     Output('ty-figure', 'config')],
    #     Input('ty-slider', 'value')
    # )
    # def update_graph(value):
    #     # print(value)

    #     request_locale  = request.accept_languages.best_match(['en_US','de_DE'])
    #     if (request_locale=='en_US'): 
    #         dash_locale = 'en'
    #         sep_locale = "."
    #         request_locale_utf8 = 'en_US.utf8'
    #     else:
    #         dash_locale = 'de'
    #         sep_locale = ","
    #         request_locale_utf8 = 'de_DE.utf8'
    #     locale.setlocale(locale.LC_ALL, request_locale_utf8)

    #     # print(request_locale_utf8)

    #     mask = (df['Year']==value)
    #     df_toDraw=df.loc[mask]
    #     df_toDraw = df_toDraw.sort_values('Market Cap', ascending=True)
    #     fig_toDraw = go.Figure(go.Bar(
    #                 x=df_toDraw['Market Cap'].tolist(),
    #                 y=df_toDraw['Name'].tolist(),
    #                 marker=dict(color=df_toDraw['Color']),
    #                 orientation='h'))

    #     # fig_toDraw.update_traces(texttemplate='%{text:.2s}',textposition='outside',textfont_size=12)

    #     fig_toDraw.update_layout(
    #         height=800,
    #         margin=dict(
    #             l=50,
    #             r=0,
    #             b=100,
    #             t=100,
    #             pad=4
    #         )
    #     )

    #     fig_toDraw.update_xaxes(
    #         tickvals=[0,50000000000,100000000000,150000000000,200000000000],
    #         range=[0,200000000000]
    #     )

       

    #     return fig_toDraw,dict(locale=dash_locale)


    return app.server