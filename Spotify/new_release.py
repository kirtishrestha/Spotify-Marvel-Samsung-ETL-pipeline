import os
import pandas as pd
from datetime import datetime
from .spotifyAPIHandler import SpotifyHandler
import json  # Import the JSON module

class NewReleaseHandler:
    def __init__(self):
        self.spotify_handler = SpotifyHandler()

    def fetch_and_save_new_releases(self):
        new_releases_data = self.spotify_handler.fetch_new_releases(limit=50, offset=0, country="US")
        all_new_releases_data = []

        for album in new_releases_data:
            album_id = album.get('id')
            name = album.get('name')
            release_date = album.get('release_date')
            total_tracks = album.get('total_tracks')
            artists = [artist['name'] for artist in album.get('artists', [])]
            artists_str = ", ".join(artists)
            href = album.get('href')
            images = [image['url'] for image in album.get('images', [])]
            images_json = json.dumps(images)  # Convert images list to JSON string
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            all_new_releases_data.append([album_id, name, release_date, total_tracks, artists_str, href, images_json, timestamp])

        df = pd.DataFrame(all_new_releases_data, columns=['album_id', 'name', 'release_date', 'total_tracks', 'artists', 'href', 'images', 'timestamp'])

        filepath = "GBD-internship/csv_files/news_raw_data/new_releases.csv"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        df.to_csv(filepath, index=False)
        print(f"Data has been written to {filepath}")

        # Load data into MySQL database
        self.spotify_handler.db.load_data(df, 'new_release')

if __name__ == "__main__":
    handler = NewReleaseHandler()
    handler.fetch_and_save_new_releases()
