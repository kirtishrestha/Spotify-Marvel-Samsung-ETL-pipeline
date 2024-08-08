from dotenv import load_dotenv
import os

dotenv_path = "C:/Users/acer/PycharmProjects/pythonProject/multiAPIProject/.env"
load_dotenv(dotenv_path)
host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")
