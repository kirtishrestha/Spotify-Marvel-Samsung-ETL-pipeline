import pandas as pd
import os
from datetime import datetime

print(os.getcwd())
file_path = 'D:/GBD-internship/csv_files/Marvel_raw_data/marvel_all_characters.csv'
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    # Load the CSV file into a DataFrame
    print('file found')
    df = pd.read_csv(file_path)
    # a new column 'popularity' based on comics appearances
    df['popularity'] = df['comics'].apply(lambda x: 'High' if x > 50 else 'Medium' if x > 20 else 'Low')
    # Split the resourceURI to get the character ID
    df['character_ids'] = df['resourceURI'].str.split('/').str[-1]
    # Get the current date and time
    current_datetime = datetime.now()
    df['data_pulled_time'] = current_datetime
    df.to_csv('../../../csv_files/marvel_news_csv_files/marvel_formatted_all_characters.csv', index=False)
    # df.to_csv('pythonProject/multiAPIProject/csv_files/marvel_csv_files/marvel_formatted_all_characters.csv', index=False)
print(f"saved in file{file_path}")
