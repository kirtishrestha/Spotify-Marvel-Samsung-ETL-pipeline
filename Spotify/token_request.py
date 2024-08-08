import requests
import base64
import json
from .config import CLIENT_ID, CLIENT_SECRET, BASE_URL, TOKEN_URL

def get_token():
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET 
    token_url = TOKEN_URL

    base_url = BASE_URL
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')
    url = token_url

    headers = {
        "authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    result.raise_for_status()
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

