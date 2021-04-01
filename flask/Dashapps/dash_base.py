import dash_bootstrap_components as dbc
import dash_html_components as html




colors = {
    'background': '#fafafa',
    'text': '#000000',
    'warning':'#FF0000'
}


def warning_card():
    return html.Br()
    return dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H5("Information", className="display-4",style={'color': colors['warning']}),
                html.P(
                    "All content on this webpage are for entertainment and information. "
                    ,
                    className="lead",
                )
            ],
            fluid=True,
        )
    ],
    fluid=True,
)