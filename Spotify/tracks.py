import os
import pandas as pd
from datetime import datetime
from .spotifyAPIHandler import SpotifyHandler
import json  # Import the JSON module

class TopTracksHandler:
    def __init__(self):
        self.spotify_handler = SpotifyHandler()

    def fetch_and_save_top_tracks(self, playlist_id):
        top_tracks_data = self.spotify_handler.fetch_top_tracks_from_playlist(playlist_id, limit=100, offset=0)
        all_tracks_data = []

        for item in top_tracks_data:
            track = item['track']
            track_id = track.get('id')
            name = track.get('name')
            album = track['album'].get('name')
            artists = [artist['name'] for artist in track['artists']]
            artists_str = ", ".join(artists)  # Convert artists list to a comma-separated string
            popularity = track.get('popularity', 0)
            duration_ms = track.get('duration_ms')
            uri = track.get('uri')
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            all_tracks_data.append([track_id, name, album, artists_str, popularity, duration_ms, uri, timestamp])

        # Create a DataFrame
        df = pd.DataFrame(all_tracks_data, columns=['track_id', 'name', 'album', 'artists', 'popularity', 'duration_ms', 'uri', 'timestamp'])

        # Save the DataFrame to a CSV file
        filepath = "GBD-internship/csv_files/news_raw_data/top_tracks.csv"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
        print(f"Data has been written to {filepath}")

        # Load data into MySQL database
        self.spotify_handler.db.load_data(df, 'tracks')

if __name__ == "__main__":
    handler = TopTracksHandler()
    playlist_id = "37i9dQZF1DXcBWIGoYBM5M"  # Replace with the actual playlist ID for the top tracks of the month
    handler.fetch_and_save_top_tracks(playlist_id)
