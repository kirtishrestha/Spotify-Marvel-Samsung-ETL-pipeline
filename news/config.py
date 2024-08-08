# News API configuration

import os
from dotenv import load_dotenv
# specify path if .env file in on another package
load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_BASE_URL = os.getenv('NEWS_BASE_URL')


