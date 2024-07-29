import dash
from dash import html, Dash
import os

def create_layout():
    img_home_page = "/assets/Application_logo.jpeg"
    current_path = os.getcwd()
    return html.Div([
        html.Div([
            html.Button('Cliquez ici', id='central-button', style={
                'position': 'absolute',
                'top': '50%',
                'left': '50%',
                'transform': 'translate(-50%, -50%)',
                'zIndex': '1'
            }),
            html.Img(src=img_home_page, style={
                'width': '100%',
                'height': '100%',
                'position': 'relative'
            })
        ], style={'position': 'relative', 'textAlign': 'center'})
    ])

def register_page(app):
    import dash
    dash.register_page(__name__, path='/', layout=create_layout())

if __name__ == '__main__':
    app = Dash(__name__)
    app.layout = create_layout()
    app.run_server(debug=True, port=8050)
