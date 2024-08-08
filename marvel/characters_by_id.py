import pandas as pd
from .marvel_handler import MarvelHandler
import json


class OneCharacterHandler(MarvelHandler):
    def fetch_specific_data(self, character_id):
        endpoint = f"characters/{character_id}"
        response_url = self.make_request(endpoint)
        response_data = json.loads(response_url)
        one_character = []
        for i in response_data['data']['results']:
            name = i['name']
            character_id = i['id']
            description = i['description']
            one_character.append([name, character_id, description])
        df = pd.DataFrame(one_character,
                          columns=['name', 'character_id', 'description'])
        print(df)
        # df.to_csv('D:/GBD-internship/csv_files/Marvel_raw_data/marvel_one_characters.csv', index=False)
        df.to_csv('../multiAPIProject/csv_files/marvel_news_csv_files/marvel_one_characters.csv', index=False)

        print("Data has been written to marvel_one_characters.csv")
