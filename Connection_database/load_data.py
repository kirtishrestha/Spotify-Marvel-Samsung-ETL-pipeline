import pandas as pd
from Connection_database.database import Database  # Ensure correct import path

def load_csv_to_sql(file_path, table_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Create a Database instance
    db = Database()
    
    # Load data into the specified table
    db.load_data(df, table_name)
    print(f"Data from {file_path} loaded into {table_name} table.")

if __name__ == "__main__":
    # Define paths to your CSV files and corresponding table names
    csv_files_and_tables = {
        "D:/GBD-internship/csv_files/news_raw_data/artist.csv": "artist",
        "D:/GBD-internship/csv_files/news_raw_data/artists.csv": "artists",
        "D:/GBD-internship/csv_files/news_raw_data/categories.csv": "category",
        "D:/GBD-internship/csv_files/news_raw_data/new_releases.csv": "new_release",
        "D:/GBD-internship/csv_files/news_raw_data/top_tracks.csv": "tracks",
    }

    # Load each CSV file into the corresponding SQL table
    for file_path, table_name in csv_files_and_tables.items():
        load_csv_to_sql(file_path, table_name)
