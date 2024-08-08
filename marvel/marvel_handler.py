import urllib3
import ssl
import time
import hashlib

from marvel import config


# import config
# from pythonProject.marvel.config import
# from pythonProject.multiAPIProject.api_handlers.marvel.marvel_data_load import config


class MarvelHandler:
    def __init__(self):
        self.api_key = config.MARVEL_API_KEY
        self.base_url = config.MARVEL_BASE_URL
        self.hash = config.MARVEL_HASH
        self.ts = config.MARVEL_TS
        self.private_key = config.PRIVATE_KEY

    def get_url(self, endpoint):
        my_ts = str(int(time.time()))
        my_hash_value = hashlib.md5((my_ts + self.private_key + self.api_key).encode('utf-8')).hexdigest()

        return f"{self.base_url}{endpoint}?apikey={self.api_key}&ts={my_ts}&hash={my_hash_value}"

    def make_request(self, endpoint):
        url = self.get_url(endpoint)
        # For SSL/TLS Compatibility
        ctx = ssl.create_default_context()
        # Comment out or adjust the cipher setting
        # ctx.set_ciphers('DEFAULT@SECLEVEL=1') <-- Commenting this out
        http = urllib3.PoolManager(ssl_context=ctx)
        response = http.request("GET", url)
        if response.status == 200:
            print("success")
            response_data = response.data.decode('utf-8')
            return response_data
        else:
            raise Exception(f"Request failed with status code: {response.status}")
