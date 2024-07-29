import dash
from dash import html, dcc, callback, Input, Output
import requests

dash.register_page(__name__)

layout = html.Div([
    html.H1('Page 1'),
    html.Button('Charger les données', id='load-button'),
    html.Div(id='data-output')
])

@callback(
    Output('data-output', 'children'),
    Input('load-button', 'n_clicks')
)
def load_data(n_clicks):
    if n_clicks is None:
        return "Cliquez sur le bouton pour charger les données"
    response = requests.get('http://localhost:8050/api/data')
    data = response.json()
    return f"Données chargées : {data['message']}"
