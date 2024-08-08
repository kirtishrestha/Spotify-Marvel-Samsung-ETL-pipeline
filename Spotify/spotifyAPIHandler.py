from .config import CLIENT_ID, CLIENT_SECRET, BASE_URL, TOKEN_URL
# from .config import
from requests import get
from .token_request import get_token, get_auth_header
import json
import requests
from Connection_database.database import Database


class SpotifyHandler():
    def __init__(self):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.token_url = TOKEN_URL
        self.base_url = BASE_URL
        self.token = get_token()
        self.db = Database()

    def get_auth_header(self):
        return {'Authorization': f'Bearer {self.token}'}

    def search_for_artists(self, artist_name):
        url = "https://api.spotify.com/v1/search"
        headers = get_auth_header(self.token)
        query = f"?q={artist_name}&type=artist&limit=20"

        query_url = url + query
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)["artists"]["items"]
        print(json_result)

        if len(json_result) == 0:
            print("No artist with this name exists...")
            return None

        return json_result[0]

    def fetch_browse_categories(self, limit=50, offset=0, country="US"):
        url = f"{self.base_url}/browse/categories"
        headers = self.get_auth_header()
        params = {
            "limit": limit,
            "offset": offset,
            "country": country
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        json_result = response.json()["categories"]["items"]
        print(json_result)

        if len(json_result) == 0:
            print("No categories found...")
            return None

        return json_result

    def fetch_new_releases(self, limit=50, offset=0, country="US"):
        url = f"{self.base_url}/browse/new-releases"
        headers = self.get_auth_header()
        params = {
            "limit": limit,
            "offset": offset,
            "country": country
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        json_result = response.json()["albums"]["items"]
        print(json_result)

        if len(json_result) == 0:
            print("No new releases found...")
            return None

        return json_result

    def fetch_top_artists_from_playlist(self, playlist_id="37i9dQZF1DXcBWIGoYBM5M", limit=100, offset=0):
        url = f"{self.base_url}/playlists/{playlist_id}/tracks"
        headers = self.get_auth_header()
        params = {
            "limit": limit,
            "offset": offset
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        json_result = response.json()["items"]
        print(json_result)

        if len(json_result) == 0:
            print("No top artists found...")
            return None

        return json_result

    def fetch_artist_details(self, artist_id):
        url = f"{self.base_url}/artists/{artist_id}"
        headers = self.get_auth_header()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def fetch_top_tracks_from_playlist(self, playlist_id, limit=100, offset=0):
        url = f"{self.base_url}/playlists/{playlist_id}/tracks"
        headers = self.get_auth_header()
        params = {
            "limit": limit,
            "offset": offset
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        json_result = response.json()["items"]
        print(json_result)

        if len(json_result) == 0:
            print("No top tracks found...")
            return None

        return json_result
