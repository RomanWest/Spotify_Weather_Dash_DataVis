import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.missing_ipywidgets import FigureWidget
from plotly.subplots import make_subplots
import plotly.graph_objects as go


import pandas as pd
import plotly.graph_objs as go
from flask import Flask

server = Flask(__name__)
server.secret_key ='test'
app = dash.Dash(name = __name__, server = server)
app.config.suppress_callback_exceptions = True

# Step 1. Launch the application
app = dash.Dash()
server = app.server

# Step 2. Import the dataset
st = pd.read_csv('Spotify_May_2020_April_2021_With_Weather.csv')

# features = st.columns[0:5]

# def get_options(features):
#     dict_list = []
#     for i in features:
#         dict_list.append({'label': i, 'value': i})

#     return dict_list


# # dropdown options
# features = st.columns[8:-1]

# opts = [{'label' : i, 'value' : i} for i in features]

fig = make_subplots(specs=[[{"secondary_y": True}]
# , [{}]
]
# rows=2, cols=1, subplot_titles=("Audio Feature and Sunshine", "Listening Time, Sunshine and Rain"), 
)

# Frames= []

# app.css.append_css({
#     'style.css'
# })

app.layout = html.Div([

                html.Div([
                html.Div([         
                # a header and a paragraph
                html.Div([
                    html.H1("Visualising One Year of Spotify Listening & The Weather", style = {'fontFamily' : 'Arial'}),],
                            style = {'padding' : '10px' ,
                            'backgroundColor' : 'rgba(250,250,250)',
                            'resize': 'both', 
                            'overflow': 'auto', 
                            'borderRadius': '1rem',
                            'titleFontFamily' : 'Arial'}),
                html.Div([html.P()]),    
                    
                html.Div([    
                    html.P("The datasets for the visualisations below were collected from analysis of my personal Spotify listening history (May 2020 to April 2021) using the Spotify API, and from the Met Office Heathrow weather station.", style = {'fontFamily' : 'Arial'}),
                    html.P("The visualisations only take into account songs that were listened to for longer than 60 seconds.", style = {'fontFamily' : 'Arial'}),],
                            style = {'padding' : '10px' ,
                            'backgroundColor' : 'rgba(250,250,250)',
                            'resize': 'both', 
                            'overflow': 'auto', 
                            'borderRadius': '1rem',
                            'titleFontFamily' : 'Arial'}),
                    
                    ],


                    style = {'padding' : '30px' ,
                            'backgroundColor' : 'rgba(30,215,96, 0.9)',
                            'resize': 'both', 
                            'overflow': 'auto', 
                            'borderRadius': '1rem',
                            'titleFontFamily' : 'Arial'}),
                    
                    
                html.Div([html.P()]),
                
# adding a plot
                html.Div([
                    dcc.Graph(id = 'plot', figure=fig)],
                    style = {
                            'resize': 'both', 
                            'overflow': 'auto',
                            'borderRadius': '1rem'}
                    ),
                html.Div([html.P()]),
                html.Div([
                    dcc.Graph(id = 'plot2', figure={
                        'data': [
                            {'x': st['Month'], 'y': st['Listening Time (Hours) Normalised and multiplied by 100'], 'type': 'line', 'name': 'Listening Time (hours)', 'line': dict(color='rgb(102,194,165)')},
                            {'x': st['Month'], 'y': st['Sun Hours  (Normalised and multiplied by 100) '], 'type': 'line', 'name': 'Sun (hours)', 'line': dict(color='rgb(252,141,98)')},
                            {'x': st['Month'], 'y': st['rain_mm (normalised) multiplied by 100'], 'type': 'line', 'name': 'Rain (mm)', 'line': dict(color='rgb(141,160,203)')}
                        ],
                        'layout': {
                            'title': {'text':'<b>Listening Time, Sunshine and Rain</b> Normalised 0-100', 'x':'0.05'},
                            'plot_bgcolor' : 'rgb(255, 255, 255)',
                            'linecolor': 'rgb(255, 255, 255)',
                            'hoverData': 'False',
                            'legend_font_family' :'Arial',
                            'yaxis' : {"gridcolor": "white", "linecolor": "white", 'hover_data': 'False'},
                            'xaxis' : {"gridcolor": "white", "linecolor": "white", 'hover_data': 'False'}
                        }
                    }),], 
                            style = { 
                                    'resize': 'both', 
                                    'overflow': 'auto',
                                    'borderRadius': '1rem'}

                    ),
                      

        ],
                        style = {'padding' : '20px' ,
                                'backgroundColor' : 'rgba(50,50,50,0.5)',
                                'resize': 'both', 
                                'overflow': 'auto', 
                                'borderRadius': '1rem'}
        ),],
                        style = {'padding' : '30px' ,
                                'backgroundColor' : 'rgba(0,0,0, 1)',
                                'resize': 'both', 
                                'overflow': 'auto', 
                                'borderRadius': '1rem'}
                )

fig.add_trace(go.Scatter(x = st['Month'], y = st['Sun Hours'],
                    fill='tozeroy', 
                    fillcolor = 'rgba(230,171,2, 0.1)',
                    name = 'Sun Hours',
                    line = dict(width = 1,
                    color = 'rgba(0,0,0)',
                    dash='dash',)),
                    secondary_y=True, 
                    # row=1, col=1
                    )

# fig.add_trace(go.Scatter(x = st['Month'], 
#                     y = st['rain_mm'],
#                     fill='tozeroy',
#                     fillcolor = 'rgba(230,171,2, 0.1)',
#                     name = 'rain_mm',
#                     line = dict(width = 2,
#                     color = 'rgb(117,112,179)')),
#                     secondary_y=True,
#                     # row=1, col=1
#                     )

fig.add_trace(go.Scatter(x = st['Month'], 
                    y = st['Acousticness'],
                    name = 'Acousticness',
                    line = dict(width = 2,
                    color = 'rgb(231,41,138)')),
                    secondary_y=False,
                    # row=1, col=1
                    )

fig.add_trace(go.Scatter(x = st['Month'], 
                    y = st['Danceability'],
                    visible='legendonly',
                    name = 'Danceability',
                    line = dict(width = 2,
                    color = 'rgb(27,158,119)')), 
                    secondary_y=False,
                    # row=1, col=1
                    )

fig.add_trace(go.Scatter(x = st['Month'], y = st['Energy'],
                    visible='legendonly',
                    name = 'Energy',
                    line = dict(width = 2,
                    color = 'rgb(217,95,2)')), 
                    secondary_y=False,
                    # row=1, col=1
                    )

fig.add_trace(go.Scatter(x = st['Month'], 
                    y = st['Instrumentalness'],
                    visible='legendonly',
                    name = 'Instrumentalness',
                    line = dict(width = 2,
                    color = 'rgb(102,166,30)')), 
                    secondary_y=False,
                    # row=1, col=1
                    )

fig.add_trace(go.Scatter(x = st['Month'], 
                    y = st['Valence'],
                    visible='legendonly', 
                    name = 'Valence',
                    line = dict(width = 2,
                    color = 'rgb(117,112,179)')),
                    secondary_y=False,
                    # row=1, col=1
                    )



# fig.add_trace(go.Scatter(x = st['Month'], y = st['Listening Time (Hours) Normalised and multiplied by 100'],
#                         name = 'Listening Time (Hours) Normalised and multiplied by 100',
#                         line = dict(width = 2, 
#                         color = 'green')),
#                         secondary_y=False,
#                         row=2, col=1)

# fig.add_trace(go.Scatter(x = st['Month'], y = st['Sun Hours  (Normalised and multiplied by 100) '],
#                         name = 'Sun Hours (Normalised and multiplied by 100)',
#                         line = dict(width = 2, 
#                         color = 'orange')),
#                         secondary_y=False,
#                         row=2, col=1)

# fig.add_trace(go.Scatter(x = st['Month'], y = st['rain_mm (normalised) multiplied by 100'],
#                         name = 'Rain_mm (normalised) multiplied by 100',
#                         line = dict(width = 2, 
#                         color = 'blue')),
#                         secondary_y=False,
#                         row=2, col=1)




fig.update_layout(
                title_text='<b>Audio Features</b> (0-1) and <b>Sun Hours</b> (0-308.6)',
                title_x=0.05,
                title_font_family='Arial',
                hovermode = 'closest',
                # yaxis_range=[0,1],
                legend_font_family='Arial',
                plot_bgcolor='rgb(255, 255, 255)', 
                spikedistance=1000,
                # Format x axis
                xaxis=dict(
                linecolor='rgb(0, 0, 0)',
                showgrid=False,
                # Show spike line for X-axis
                showspikes=True, 
                # Format spike
                spikethickness=2,
                spikedash="dot",
                spikecolor="#999999",
                spikemode="across",
                ),
                # Format y axis
                yaxis=dict(
                spikethickness=2,
                linecolor='rgb(255, 255, 255)',
                showgrid=False
                ),
                # updatemenus=[dict(
                # type="buttons",
                # buttons=[dict(label="Play",
                # method="animate",
                # args=[None])])],
                ), 
               

fig.update_yaxes(
    secondary_y=True)

fig.update_yaxes(
    secondary_y=False)

# fig.update_xaxes(
#     title_text="<b>Month</b>", automargin=True)



# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)

# fig.add_trace(go.Scatter(x = st['Month'],
#                     y=st['Energy']+st['Energy (SD.P)'],
#                     name = 'Energy Upper Bound',
#                     line = dict(width = 0,
#                     color = 'rgb(217,95,2, 0.1)')), 
#                     secondary_y=False,
#                     )

# fig.add_trace(go.Scatter(x = st['Month'],
#                     y=st['Energy']-st['Energy (SD.P)'],
#                     name = 'Energy Lower Bound',
#                     fill='tonexty',
#                     line = dict(width = 0,
#                     color = 'rgb(217,95,2, 0.1)')),
#                     secondary_y=False,
#                     )

# fig.add_trace(go.Scatter(x = st['Month'],
#                     y=st['Instrumentalness']+st['Instrumentalness (SD.P)'],
#                     name = 'Instrumentalness Upper Bound',
#                     line = dict(width = 0,
#                     color = 'rgb(102,166,30, 0.1)')), 
#                     secondary_y=False,
#                     )

# fig.add_trace(go.Scatter(x = st['Month'],
#                     y=st['Instrumentalness']-st['Instrumentalness (SD.P)'],
#                     name = 'Instrumentalness Lower Bound',
#                     fill='tonexty',
#                     line = dict(width = 0,
#                     color = 'rgb(102,166,30, 0.1)')),
#                     secondary_y=False,
#                     )

# fig.add_trace(go.Scatter(x = st['Month'],
#                     y=st['Danceability']+st['Danceability (SD.P)'],
#                     name = 'Danceability Upper Bound',
#                     line = dict(width = 0,
#                     color = 'rgb(27,158,119, 0.1)')), 
#                     secondary_y=False,
#                     )

# fig.add_trace(go.Scatter(x = st['Month'],
#                     y=st['Danceability']-st['Danceability (SD.P)'],
#                     name = 'Danceability Lower Bound',
#                     fill='tonexty',
#                     line = dict(width = 0,
#                     color = 'rgb(27,158,119, 0.1)')),
#                     secondary_y=False,
#                     )

# fig.add_trace(go.Scatter(x = st['Month'],
#                     y=st['Valence']+st['Valence (SD.P)'],
#                     name = 'Valence Upper Bound',
#                     mode='lines',
#                     line = dict(width = 0,
#                     color = 'rgb(117,112,179, 0.1)')), 
#                     secondary_y=False,
#                     )

# fig.add_trace(go.Scatter(x = st['Month'],
#                     y=st['Valence']-st['Valence (SD.P)'],
#                     name = 'Valence Lower Bound',
#                     mode='lines',
#                     fill='tonexty',
#                     line = dict(width = 0,
#                     color = 'rgb(117,112,179, 0.1)')),
#                     secondary_y=False,
#                     )

# fig.add_trace(go.Scatter(x = st['Month'],
#                     y=st['Acousticness']+st['Acousticness (SD.P)'],
#                     name = 'Acousticness Upper Bound',
#                     mode='lines',
#                     line = dict(width = 0,
#                     color = 'rgb(231,41,138, 0.1)')), 
#                     secondary_y=False,
#                     )

# fig.add_trace(go.Scatter(x = st['Month'],
#                     y=st['Acousticness']-st['Acousticness (SD.P)'],
#                     name = 'Acousticness Lower Bound',
#                     mode='lines',
#                     fill='tonexty',
#                     line = dict(width = 0,
#                     color = 'rgb(231,41,138, 0.1)')),
#                     secondary_y=False,
#                     )
