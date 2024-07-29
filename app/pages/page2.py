# pages/page2.py
import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.H1('Page 2'),
    html.P("Contenu de la page 2")
])