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
from plotly.subplots import make_subplots
from ..Dash_base import warning_card, colors
import dash_table
from datetime import datetime
import numpy as np
from flask import request
import locale
import pycountry_convert  as pc


url_base = '/dash/app14/' 



data_sources = [
    "https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021",
    "https://www.kaggle.com/danielkorth/eda-world-happiness-report-2021",
]   

data_licenses = [
    "https://creativecommons.org/publicdomain/zero/1.0/"
]

df = pd.read_csv('app_data/processed/0009.csv')

# temp = df.sort_values(by=['Ladder score'], ascending=False)



df2 = df.set_index('Country name')
temp = pd.DataFrame(df2['Perceptions of corruption']).reset_index()

#ADAPTING TO THE ISO 3166 STANDARD
temp.loc[temp['Country name'] == 'Taiwan Province of China', 'Country name'] = 'Taiwan, Province of China' 
temp.loc[temp['Country name'] == 'Hong Kong S.A.R. of China', 'Country name'] = 'Hong Kong' 
temp.loc[temp['Country name'] == 'Congo (Brazzaville)','Country name'] = 'Congo' 
temp.loc[temp['Country name'] == 'Palestinian Territories','Country name'] = 'Palestine, State of' 

temp.drop(index=temp[temp['Country name'] == 'Kosovo'].index, inplace=True) # Kosovo Code agreed on not to use by ISO 3166
temp.drop(index=temp[temp['Country name'] == 'North Cyprus'].index, inplace=True) # Not part of the ISO 3166 standard


temp['iso_alpha'] = temp['Country name'].apply(lambda x:pc.country_name_to_country_alpha3(x,))
temp2 = temp.sort_values(by=['Perceptions of corruption'], ascending=False)[:20]
fig = px.choropleth(temp, locations='iso_alpha',
                    color='Perceptions of corruption',
                    hover_name='Country name',
                    color_continuous_scale=px.colors.diverging.Picnic,
                   )
fig.update_layout(
    showlegend=False,
    paper_bgcolor='rgb(248, 248, 255)',
    geo_bgcolor='rgb(248, 248, 255)',
    geo_showframe=False,
    height=600,
    legend={"xanchor":"center", "yanchor":"top"},
    margin=dict(
        l=0,
        r=0,
        b=50,
        t=50
    )
)
###

t1 = temp.nlargest(20, 'Perceptions of corruption')[::-1]
fig2 = make_subplots(rows=1, cols=2, 
                    column_widths=[0.65, 0.35],
                    subplot_titles=['Top 20 Countries', 'All countries'])
fig2.append_trace(go.Bar(x=t1['Perceptions of corruption'],
                y=t1['Country name'],
                orientation='h',
           
                marker=dict(
                    color=colors['gray'],
                    line=dict(color=colors['black'], width=1)
                ),
                        name=''
               ), 1,1
             )

fig2.append_trace(go.Box(y=df['Perceptions of corruption'],
                        marker_color=colors['lightgray'],
                        name=''), 1,2)
fig2.add_vline(x=9,
              col=1,
              )

fig2.update_layout(
    xaxis_range=(0.8,0.95),
    yaxis2_range=(0.35,1),
    xaxis = {                              
    'showgrid': True,
    'gridcolor' :colors['gray'],
    'tickfont': {
        'color': '#333',
        'size': 12
      },
    },
    yaxis2 = {                              
    'showgrid': False,
    # 'mirror': True,
    # 'automargin':False,
    'side':'right',
    'anchor': 'free',
    'position': 0.95,
    'gridcolor' :colors['gray'],
    'tickfont': {
        'color': '#333',
        'size': 12
      },
    },
    margin=dict(
        l=0,
        r=0,
        b=50,
        t=100
    ),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    showlegend=False,
    title_text='Top 20 Countries',
    title_font_size=22),
    
fig2.update_annotations(yshift=5)


def description_card():
    return html.Div(
        id="description_card",
        children = [dcc.Markdown(''' On the map below you see the a score that measures the perception of people on corruption in their country. The score ranges from 0 to 1. The results are gathered from the Gallup World Poll. Below the map you will also find a list of the Top 20 countries based on the score.''')],
    style={
        'backgroundColor': colors['background'],
    })



# The Layout
layout = html.Div(style={'font-family':'"Poppins", sans-serif', 'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Perceptions of corruption in each country',
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
        id='ty-figure',
        figure=fig
    ),
    dcc.Graph(
        id='ty-figure2',
        figure=fig2
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

    return app.server