# Marvel API configuration
from dotenv import load_dotenv
import os  # interact with the operating system and allows you to access environment variables
import time
import hashlib
load_dotenv()
MARVEL_API_KEY = os.getenv('MARVEL_API_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
MARVEL_BASE_URL = os.getenv('MARVEL_BASE_URL')

MARVEL_TS = str(time.time())
to_hash = MARVEL_TS + MARVEL_API_KEY + PRIVATE_KEY
MARVEL_HASH = hashlib.md5(to_hash.encode('utf-8')).hexdigest()
