An Interactive data visualisation dashboard of my Spotify listening history using the Spotify/Echnoest API and Met Office weather data.

The visualisations are built using Plotly/Dash.

The datasets for the visualisations were collected from analysis of my personal Spotify listening history (May 2020 to April 2021) using the Spotify API (Echonest), and from the Met Office Heathrow weather station.

The visualisations only take into account songs that were listened to for longer than 60 seconds.

To run DashApp

    Locate the source folder (the one containing app.py) in the terminal/command line

    Start a virtual environment Option 1) python3 -m venv venv source venv/bin/activate Option 2) py -m venv venv cd venv\Scripts\activate

    Return to main folder: cd \Spotify_Weather_Dash_DataVis-main

    pip install -r requirements.txt

    python app.py or py app.py

