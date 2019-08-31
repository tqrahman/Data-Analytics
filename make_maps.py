# Dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

# Data tools imports
import pandas as pd

# Mapping Imports
import plotly.graph_objects as go

mapbox_access_token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w'

# Reading in the data
df = pd.read_csv("map.csv")

# Function to make the map

def map_now(df):
    layout = dict(
        autosize=True,
        hovermode="closest",
        showlegend=False,
        mapbox=dict(
            accesstoken=mapbox_access_token,
            style="light",
            center=dict(
                lon=df['longitude'].mean(),
                lat=df['latitude'].mean()
            ),
            zoom=14,
        ),
        clickmode='event+select'
    )
    d = [
        go.Scattermapbox(
            lat = df['latitude'].tolist(),
            lon = df['longitude'].tolist(),
            mode='markers',
            marker=go.scattermapbox.Marker(size=9),
            text=df['type'].tolist()
        )
    ]
    figure = dict(data=d, layout=layout)
    return figure

### Dashboard ###

EXTERNAL_STYLESHEETS = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)
app.config['suppress_callback_exceptions']=True

app.layout = html.Div([

    # Title
    html.H1("Map"),

    html.Div([
        dcc.Graph(id='map',
                  figure=map_now(df))
    ])
])

### RUNNING APP ###

if __name__ == '__main__':
    app.run_server(debug=True)
