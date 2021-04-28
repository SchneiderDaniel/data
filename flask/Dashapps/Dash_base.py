import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc




colors = {
    'background': '#fafafa',
    'text': '#000000',
    'warning':'#FF0000',
    'info':'#6e7278',
    'green1':'#9fb557',
    'green2':'#76b557',
    'gray':'#7f8280',
    'black':'#202121',
    'lightgray':'#acb5b5',
    'superlightgray':'#e9ecef'
}

def cite_card(cite_text,cite_author,cite_link):
    return dbc.Container(
        [
            html.Br(),
            html.P(f"{cite_text}", style={
                    'textAlign': 'left',
                    'color': colors['text']
                    }),
            html.Hr(),
            html.P(f" by {cite_author}", style={
                    'textAlign': 'right',
                    'color': colors['text']
                    }),
            dbc.NavLink(f" \u2192 Info",href=cite_link, target='_blank', style={
                    'textAlign': 'right',
                    'color': colors['text'],
                    'font-style': 'italic',
                   }),
            # html.Br(),
        ],style={
                       'backgroundColor': colors['superlightgray'],
                       'font-family':'"Poppins", sans-serif',
                   },
    )
def warning_card(data_sources,data_licenses, source_date="<na>"):
    return dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H3("Information",style={'color': colors['info']}),
                html.P(
                    "All contents on this webpage are for entertainment and information. We source our data from freely available data on the internet. Below you can find a list of all the sources that were used to create the content on this exact page. Moreover, we also add the license references, in case they are available.  "
                    ,
                    className="lead",
                ),
                html.H4("Sources and Licenses:", style={'color': colors['info']}),
                get_link_list(data_sources,"Source"),
                get_link_list(data_licenses,"License"),
                html.P("Data sourced on: " + source_date),
                dbc.Alert(
                        [
                            "In case you are the owner of one of the data sources and you are not ok with the usage on this page, you can contact us ",
                            html.A("here", href='https://blackandwhitedata.com/contact/', target='_blank', className="alert-link"),
                        ],
                        color="primary",
                    ),
            ],
            fluid=True,
        )
    ],
    fluid=True,
)

def get_link_list(link_list, name):

    list_group = dbc.ListGroup(children=[])

    if len(link_list)==0:
        list_group.children.append(
                dbc.ListGroupItem(
                    "No " + name + " available" )
            )
        return list_group
    else:
        for i in range(len(link_list)):
            list_group.children.append(
                dbc.ListGroupItem(
                    name + " #" +  str(i+1), href=link_list[i], target='_blank'
                )
            )
    return list_group
