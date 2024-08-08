from dotenv import load_dotenv
import os # os is a module that provides a way to work with operating system dependent functionality
# specify path if .env file in on another package
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TOKEN_URL = os.getenv('TOKEN_URL')
BASE_URL = os.getenv('BASE_URL')

