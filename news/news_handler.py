import requests

from news.config import NEWS_API_KEY, NEWS_BASE_URL


# from news.config import NEWS_API_KEY, NEWS_BASE_URL


class NewsHandler:
    def __init__(self):
        self.NEWS_API_KEY = NEWS_API_KEY
        self.NEWS_BASE_URL = NEWS_BASE_URL

    def get_url(self, endpoint):
        q = 'samsung'
        from_time = '2024-06-17'
        sort_by = 'popularity'
        country = 'us'
        category = 'technology'
        if endpoint == 'everything':
            return f"{self.NEWS_BASE_URL}{endpoint}?apiKey={self.NEWS_API_KEY}&q={q}&from={from_time}&sortBy={sort_by}"
        elif endpoint == 'top-headlines':
            return f"{self.NEWS_BASE_URL}{endpoint}?apiKey={self.NEWS_API_KEY}&country={country}&category={category}"
        else:
            raise Exception(f"Request failed with invalid endpoint: {endpoint}")

    def make_request(self, endpoint):
        url = self.get_url(endpoint)
        response = requests.get(url)
        print("news response", response)
        if response.status_code == 200:
            print("success")
            data = response.json()
            return data
        else:
            raise Exception(f"Request failed with status code: {response.status_code}")
