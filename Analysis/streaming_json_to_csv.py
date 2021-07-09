from __future__ import print_function 
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys 
import pandas as pd
import numpy as np
from collections import OrderedDict
from math import log
import json
import spotipy.util as util
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
import requests

username = #add here
client_id = #add here
client_secret = #add here
redirect_uri = 'http://example.com/callback/'
scope = 'user-read-recently-played'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)
with open('StreamingHistory1.json', encoding='utf8') as f:
    data = json.load(f)

spotify_data = pd.DataFrame()

def extract_json_value(column_name):
    
    return [i[column_name] for i in data]

spotify_data['artist_name'] = extract_json_value('artistName')
spotify_data['end_time'] = extract_json_value('endTime')
spotify_data['ms_played'] = extract_json_value('msPlayed')
spotify_data['track_name'] = extract_json_value('trackName')

# function to get track_id
def get_id(track_name: str,artist:str, token: str) -> str:
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer ' + token,
    }
    track_artist = track_name+ " " + artist
    params = [
    ('q',track_artist ),#q is the search query parameter
    ('type', 'track'),
    ]
    try:
        response = requests.get('https://api.spotify.com/v1/search', 
                    headers = headers, params = params, timeout = 10)
        json = response.json()
        first_result = json['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except:
        return None

# Get track_id for streaming history    
spotify_data["track_id"] = spotify_data.apply(lambda x: get_id(x["track_name"],
                                                               x["artist_name"],
                                                                 token),axis=1)



spotify_data.to_csv("streaming_json_to_CSV_pt2.csv")