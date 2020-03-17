import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

app = dash.Dash()

# Creating DATA

df = pd.read_csv('Data_ ReliefWeb Crisis Figures Data - latest_figures.csv')

app.layout = html.Div([
    Html.Label("Countries")
    div.Dropdown(id="dropdown", Options=[{"label":"crisis.crisis_name","value":"crisis.crisis_iso3", Value="crisis.crisis_iso3"}]
         dcc.Markdown(),

        dcc.Graph(id='scatterplot',
                    figure = {'data':[
                            go.Scatter(
                            x=,
                            y=,
                            mode='markers',
                            marker = {
                                'size':12,
                                'color': 'rgb(51,204,153)',
                                'symbol':'pentagon',
                                'line':{'width':2}
                            }
                            )],
                    'layout':go.Layout(title='title',
                                        yaxis = {'title':'-'})}
                    ),
dcc.Markdown(),

                   

                    dcc.Graph(id='scatterplot2',
                    figure = {'data':[
                            go.Scatter(
                            x=,
                            y=,
                            mode='markers',
                            marker = {
                                'size':12,
                                'color': 'rgb(51,204,153)',
                                'symbol':'pentagon',
                                'line':{'width':2}
                            }
                            )],
                    'layout':go.Layout(title='Goal Difference',
                                        yaxis = {'title':'-'})}
                    ),

dcc.Markdown(),

        dcc.Graph(id='Bar',
                     figure = {'data':[
                            go.Bar(
                            x=,
                            y=,
                            name='hhh',
                            ),
                            go.Bar(
                            x=,
                            y=,
                            name='lll',
                            ),
                            go.Bar(
                            x=,
                            y=,
                            name='',
                            )
                     
                            
                            ],
                    'layout':go.Layout(title='title',
                                        yaxis = {'title':'-'})}
                    ),
                    
 dcc.Markdown(),
   
                    dcc.Graph(id='pie',
                                        figure = {'data':[
                                                go.Pie(
                                                values = ,
                                                labels= 
                                                )],
                                        'layout':go.Layout(title='title',
                                         yaxis = {'title':'-'})}
                                        )])

                       
                   

if __name__ == '__main__':
    app.run_server(debug=True)