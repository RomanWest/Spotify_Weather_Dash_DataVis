import pandas as pd
import csv

artist_name_data = pd.read_csv('streaming_json_to_CSV_pt2.csv')
artist_name_data_nonull = artist_name_data.dropna(axis=0, how='any')
artist_name_data_nonull.to_csv('artist_name_data_nonull2.csv')

artist_name_data_nonull = pd.read_csv('artist_name_data_nonull2.csv')

streaming_features = pd.read_csv('streaming_track_feature2.csv')

merged = artist_name_data_nonull.merge(streaming_features, on='song_id')

merged.to_csv('merged_artist_with_track_features2.csv')