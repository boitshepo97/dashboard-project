import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

app = dash.Dash()

# Creating DATA

df = pd.read_csv('Data_ ReliefWeb Crisis Figures Data - latest_figures.csv')
labels = df.crisis_name
app.layout = html.Div([
        dcc.Markdown('''
####
The Latest Figures dataset contains information on the world’s most pressing humanitarian crises. The data, curated by ReliefWeb’s editorial team based on its relevance to the humanitarian community, is updated daily''')],
    
        dcc.Graph(id='Bar',
                     figure = {'data':[
                            go.Pie(
                            x=df.crisis_name,
                            y=df.crisis_ios3
                            )],
                    'layout':go.Layout(title='People In need Of Assistance',
                                        yaxis = {'title':'Stats'})},
        
if __name__ == '__main__':
    app.run_server(debug=True)