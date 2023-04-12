from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import numpy as np

#Load th ataset
avocado=pd.read_csv('avocado-updated-2020.csv')

app=Dash(__name__)

app.layout=html.Div(
    children=[
        html.H1(children='Avocado Prices Dashboard'),
        dcc.Dropdown(
            id='geo-dropdown',
            options=[{'label':i,'value':i} for i in avocado['geography'].unique()],
            value='New York'
            
        ),
        dcc.Graph(id='price-graph')
    ])


@app.callback (
    Output(component_id='price-graph',component_property='figure'),
    Input(component_id='geo-dropdown',component_property='value')
)
def update_graph(selected_geography):
    filtered_avocado=avocado[avocado['geography']==selected_geography]
    line_fig=px.line(
        filtered_avocado,
        x='date',
        y='average_price',
        color='type',
        title=f'Avocado Prices in {selected_geography}'
    )

    return line_fig


if __name__=='__main__':
    app.run_server(debug=True)
