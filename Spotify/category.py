import os
import json
import pandas as pd
from datetime import datetime
from .spotifyAPIHandler import SpotifyHandler

class CategoryHandler:
    def __init__(self):
        self.spotify_handler = SpotifyHandler()

    def fetch_and_save_categories(self):
        categories_data = self.spotify_handler.fetch_browse_categories(limit=50, offset=0, country="US")
        all_categories_data = []

        for category in categories_data:
            category_id = category.get('id')
            name = category.get('name')
            href = category.get('href')
            icons = json.dumps([icon['url'] for icon in category.get('icons', [])])  # Convert to JSON
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")

            all_categories_data.append([category_id, name, href, icons, date, time])


            # Convert to DataFrame for direct database loading
            category_df = pd.DataFrame([{
                'ID': category_id,
                'Name': name,
                'Href': href,
                'Icons': icons,
                'Date': date,
                'Time': time
            }])

            # Load data into MySQL database
            self.spotify_handler.db.load_data(category_df, 'categories')

        # Export all data to a CSV file
        df = pd.DataFrame(all_categories_data, columns=['ID', 'Name', 'Href', 'Icons', 'Date', 'Time'])
        filepath = "GBD-internship/csv_files/news_raw_data/categories.csv"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
        print(f"Data has been written to {filepath}")

if __name__ == "__main__":
    handler = CategoryHandler()
    handler.fetch_and_save_categories()
