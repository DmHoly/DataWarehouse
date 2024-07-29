# app.py
from flask import Flask, jsonify
from dash import Dash, html, dcc, page_container
import dash

# Configuration de l'application Flask
server = Flask(__name__)

# Configuration de l'application Dash
app = Dash(__name__, server=server, use_pages=True,
           suppress_callback_exceptions=True,
           update_title=None)

# Définition de la mise en page principale
app.layout = html.Div([
    html.H1('Mon Application Multi-pages'),
    html.Div([
        dcc.Link('Accueil', href='/'),
        dcc.Link('Page 1', href='/page1'),
        dcc.Link('Page 2', href='/page2'),
    ]),
    page_container
])

# API REST
@server.route('/api/data')
def get_data():
    # Simuler des données provenant d'une base de données
    data = {"message": "Données de l'API"}
    return jsonify(data)

# Démarrage de l'application
if __name__ == '__main__':
    app.run_server(debug=False, host='127.0.0.1', port=8050)

# Le reste du code (pages/home.py, pages/page1.py, pages/page2.py) reste inchangé