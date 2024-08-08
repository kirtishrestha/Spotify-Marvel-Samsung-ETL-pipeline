import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.host = os.getenv('MYSQL_HOST')
        self.port = os.getenv('MYSQL_PORT')
        self.user = os.getenv('MYSQL_USER')
        self.password = os.getenv('MYSQL_PASSWORD')  # Make sure this is set correctly
        self.db_name = os.getenv('MYSQL_DB')
        
        # Debug print
        print(f"Host: {self.host}, Port: {self.port}, User: {self.user}, DB: {self.db_name}")

        self.engine = self.create_db_engine()

    def create_db_engine(self):
        try:
            engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}')
            connection = engine.connect()
            print("Database connection successful!")
            connection.close()
        except Exception as e:
            print(f"Database connection failed: {e}")
            return None
        return engine

    def load_data(self, df, table_name):
        if self.engine is not None:
            df.to_sql(table_name, con=self.engine, if_exists='append', index=False)
        else:
            print("No connection to the database. Cannot load data.")

if __name__ == "__main__":
    db = Database()
