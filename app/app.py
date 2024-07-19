from flask import Flask, jsonify, request
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import requests

# Backend: DataManager class
class DataManager:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def get_data(self):
        return self.data
    

# Initialize Flask app
server = Flask(__name__)
data_manager = DataManager()

# API route to add data
@server.route('/api/add', methods=['POST'])
def add_data():
    item = request.json.get('item')
    data_manager.add_data(item)
    return jsonify({'status': 'success', 'data': data_manager.get_data()})

# API route to get data
@server.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'data': data_manager.get_data()})

# Initialize Dash app
app = dash.Dash(__name__, server=server, url_base_pathname='/')

app.layout = html.Div([
    dcc.Input(id='input-box', type='text'),
    html.Button('Submit', id='button'),
    html.Div(id='output-container'),
    dash_table.DataTable(
        id='data-table',
        columns=[{'name': 'Item', 'id': 'item'}],
        data=[]
    )
])

@app.callback(
    [Output('output-container', 'children'),
     Output('data-table', 'data')],
    [Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')]
)
def update_output(n_clicks, value):
    if n_clicks is not None and value:
        response = requests.post('http://127.0.0.1:5000/api/add', json={'item': value})
        if response.status_code == 200:
            data = response.json().get('data')
            return f'Current Data: {data}', [{'item': item} for item in data]
    return 'Enter a value and press submit', []

if __name__ == '__main__':
    server.run(debug=True)