import pandas as pd
import json
import os
from marvel.marvel_handler import MarvelHandler



# from pythonProject.marvel.marvel_handler import MarvelHandler


# from marvel_handler import MarvelHandler
# from .marvel.marvel_handler import MarvelHandler
# from .marvel_handler import MarvelHandler
# from marvel_handler import MarvelHandler


class AllCharactersHandler(MarvelHandler):

    def fetch_all_characters(self):
        endpoint = "characters"
        response_url = self.make_request(endpoint)
        response_data = json.loads(response_url)
        all_characters = []
        for response in response_data['data']['results']:
            name = response['name']
            thumbnail = response['thumbnail']['path']
            resource_uri = response['resourceURI']
            comics = response['comics']['available']
            # comics_items = response['comics']['items'][0]['name']
            series = response['series']['available']
            stories = response['stories']['available']
            events = response['events']['available']
            all_characters.append(
                [name, thumbnail, resource_uri, comics, events])
        df = pd.DataFrame(all_characters,
                          columns=['name', 'thumbnail', 'resourceURI', 'comics', 'events'])
        # df.to_csv('api_handlers/marvel/marvel_csv_files/marvel_all_characters.csv', index=False)
        # df.to_csv('D:/GBD-internship/csv_files/Marvel_raw_data/marvel_all_characters.csv', index=False)
        # df.to_csv('pythonProject/multiAPIProject/csv_files/marvel_csv_files/marvel_all_characters.csv',
        #           index=False)
        # Define the relative path to the target directory
        target_directory = '../multiAPIProject/csv_files/marvel_news_csv_files'
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        # Define the file path
        file_path = os.path.join(target_directory, 'marvel_all_characters.csv')
        df.to_csv(file_path, index=False)

        print("Data has been written to marvel_all_characters.csv")
