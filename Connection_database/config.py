from dotenv import load_dotenv
import os

load_dotenv 
host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
# password = os.getenv("MYSQL_PASSWORD")
port = os.getenv("MYSQL_PORT")
