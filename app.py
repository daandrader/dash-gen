# basic dashboard implementation using dash 
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from sklearn.datasets import load_iris


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# data
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['clase'] =  iris.target
df['clase'] = df['clase'].astype('string')



# figure definition
fig_scatter = px.scatter(df, x='sepal length (cm)', y='sepal width (cm)', color='clase', template="plotly_white", title='Scatter Plot')
fig_box = px.box(df, x='clase', y='sepal length (cm)', color='clase', template='plotly_white', title = 'Multiple Boxplot')
fig_line = px.line(df, x=[1,2,3,4,5], y=[1,4,9,16,25], template='plotly_white', title='Line Plot')
fig_line.update_traces(mode='markers+lines')
fig_bar = px.bar(df, x=['S1','S2','S3'], y=[1,4,9], title='Barplot', template='plotly_white')

# layout
app.layout = html.Div(children=[
    html.H1(children='Dashboard template using Dash and plotly Libraries', className='text-center mt-5'),
    html.Hr(),
    html.Div([dbc.Alert(color='dark', children='Template by Daniel Andrade', className='mx-5')]),
    html.Div(['Dash is a web application framework for Python that generate dashboard web based apps.\
        This template is using the Dash Bootstrap Components ', html.A('[DBC]', href='https://dash-bootstrap-components.opensource.faculty.ai/'), '.'],
        className='mx-5'),

    dcc.Graph(
        id='scatter',
        figure=fig_scatter,
        style={'display': 'inline-block', 'width': '50%'}
    ),

    dcc.Graph(
        id='boxplot',
        figure=fig_box,
        style={'display': 'inline-block', 'width': '50%'}
    ), 
    
    dcc.Graph(
        id='lineplot',
        figure=fig_line,
        style={'display': 'inline-block','width': '50%'}     
    ),
    
    dcc.Graph(
        id='barplot',
        figure=fig_bar,
        style={'display': 'inline-block','width': '50%'}     
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
