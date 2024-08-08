import os
import pandas as pd
from datetime import datetime
from Spotify.spotifyAPIHandler import SpotifyHandler

class TopArtistsHandler:
    def __init__(self):
        self.spotify_handler = SpotifyHandler()

    def fetch_and_save_top_artists(self):
        top_artists_data = self.spotify_handler.fetch_top_artists_from_playlist(limit=100, offset=0)
        all_artists_data = []

        artist_ids = set()
        for item in top_artists_data:
            for artist in item['track']['artists']:
                if artist['id'] not in artist_ids:
                    artist_ids.add(artist['id'])
                    artist_info = {
                        'id': artist['id'],
                        'name': artist['name'],
                        'href': artist['href'],
                        'uri': artist['uri']
                    }
                    all_artists_data.append(artist_info)

        detailed_artists_data = []
        for artist in all_artists_data:
            artist_info = self.spotify_handler.fetch_artist_details(artist['id'])
            genres = ", ".join(artist_info.get('genres', []))
            followers = artist_info.get('followers', {}).get('total', 0)
            popularity = artist_info.get('popularity', 0)
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            detailed_artists_data.append([
                artist_info.get('id'),
                artist_info.get('name'),
                genres,
                followers,
                popularity,
                artist_info.get('uri'),
                timestamp
            ])

        # Create DataFrame
        df = pd.DataFrame(detailed_artists_data,
                          columns=['artist_id', 'name', 'genres', 'followers', 'popularity', 'uri', 'timestamp'])

        # Save to CSV (optional, for backup or debugging purposes)
        filepath = "GBD-internship/csv_files/news_raw_data/top_artists.csv"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
        print(f"Data has been written to {filepath}")

        # Load DataFrame into MySQL database
        self.spotify_handler.db.load_data(df, 'artists')

if __name__ == "__main__":
    handler = TopArtistsHandler()
    handler.fetch_and_save_top_artists()
