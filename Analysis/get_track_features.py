from __future__ import print_function    # (at top of module)
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
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
import random


with open('StreamingHistory1.json', encoding='utf8') as f:
    data = json.load(f)

spotify_data = pd.DataFrame()

def extract_json_value(column_name):
    
    return [i[column_name] for i in data]

spotify_data['artist_name'] = extract_json_value('artistName')
spotify_data['end_time'] = extract_json_value('endTime')
spotify_data['ms_played'] = extract_json_value('msPlayed')
spotify_data['track_name'] = extract_json_value('trackName')

import spotipy.util as util

username = #add here
client_id = #add here
client_secret = #add here
redirect_uri = 'http://example.com/callback/'
scope = 'user-read-recently-played'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False


token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)

# Now you can finally authorize your app. Once you click on Agree, 
# you will be taken to the Redirect URI, which may well be a nonexistent page. 
# Just copy the address and paste it in your Python console.

# obtain the track_IDs by using the API to search the name of our track, 
import requests

# write the function to get track_id
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

spotify_data_nonull = spotify_data["track_id"].dropna()

track = list(OrderedDict.fromkeys(spotify_data_nonull)) 


# get track's feature
my_feature = pd.DataFrame(columns=["song_id","energy",
                                "liveness","tempo","speechiness",
                                "acousticness","instrumentalness","danceability",
                                "duration_ms","loudness","valence",
                                "mode","key"])

for song in track:
    features = sp.audio_features(tracks = [song])[0]
    thisSleep = random.randint(0,10)*0.02
    time.sleep(thisSleep)
    if features is not None:
        my_feature = my_feature.append({"song_id":song,
                                    "energy":features['energy'], 
                                    "liveness":features['liveness'],
                                    "tempo":features['tempo'],
                                    "speechiness":features['speechiness'],
                                    "acousticness":features['acousticness'],
                                    "instrumentalness":features['instrumentalness'],
                                    "danceability":features['danceability'],
                                    "duration_ms":features['duration_ms'],
                                    "loudness":features['loudness'],
                                    "valence":features['valence'],
                                    "mode":features['mode'],
                                    "key":features["key"],
                                    },ignore_index=True)
    else:
        pass

my_feature.to_csv("streaming_track_feature2.csv")
# my_feature =pd.read_csv("streaming_track_feature.csv", encoding='utf-8-sig')
# spotify_data.to_csv("streaming_trackid.csv",)

# my_streaming = pd.merge(spotify_data,my_feature,how="left",left_on= "track_id", right_on="song_id")

# # my_streaming.drop(my_streaming[my_streaming["ms_played"]==0].index,inplace=True)

# my_streaming.to_csv("my_streaming.csv")