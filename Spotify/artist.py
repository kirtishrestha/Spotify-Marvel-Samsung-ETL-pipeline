import os
import pandas as pd
from datetime import datetime
from Spotify.spotifyAPIHandler import SpotifyHandler

class ArtistsHandler:
    def __init__(self):
        self.spotify_handler = SpotifyHandler()

    def fetch_and_save_artists(self, artist_names):
        all_artists_data = []

        for artist_name in artist_names:
            artist_info = self.spotify_handler.search_for_artists(artist_name)
            if artist_info:
                artist_id = artist_info['id']
                name = artist_info.get('name')
                genres = ", ".join(artist_info.get('genres', []))
                followers = artist_info.get('followers', {}).get('total', 0)
                popularity = artist_info.get('popularity', 0)
                uri = artist_info.get('uri', '')
                now = datetime.now()
                date = now.strftime("%Y-%m-%d")
                time = now.strftime("%H:%M:%S")


                # Append to list for CSV export
                all_artists_data.append([artist_id, name, genres, followers, popularity, uri, date, time])

                # Convert to DataFrame for direct database loading
                artist_df = pd.DataFrame([{
                    'artist_id': artist_id,
                    'name': name,
                    'genres': genres,
                    'followers': followers,
                    'popularity': popularity,
                    'uri': uri,
                    'date': date,
                    'time': time
                }])

                # Load data into MySQL database
                self.spotify_handler.db.load_data(artist_df, 'artist')

        # Export all data to a CSV file
        df = pd.DataFrame(all_artists_data, columns=['artist_id', 'name', 'genres', 'followers', 'popularity', 'uri', 'date', 'time'])
        filepath = "GBD-internship/csv_files/news_raw_data/artist.csv"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
        print(f"Data has been written to {filepath}")

if __name__ == "__main__":
    artist_names = ["Adele", "Ed Sheeran", "Taylor Swift", "Cynthia Erivo", "Isabel LaRosa", "Lorde", "Mitski", "The Weeknd", "Måneskin", "The Neighbourhood"]
    
    handler = ArtistsHandler()
    handler.fetch_and_save_artists(artist_names)
