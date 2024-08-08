# from api_handlers.factory import HandlerFactory
# main.py(starting of the project)
# from multiAPIProject.api_handlers.factory import HandlerFactory
from .api_handlers.factory import HandlerFactory


def main():
    # Create a Marvel API handler
    marvel_all_characters_handler = HandlerFactory.get_handler('marvel', 'all_characters')
    all_characters_df = marvel_all_characters_handler.fetch_all_characters()
    print("my all character", all_characters_df)

    # Fetch details of a specific character(iron man)
    marvel_one_character_handler = HandlerFactory.get_handler('marvel', 'one_character')
    character_id = 1009368
    one_character_df = marvel_one_character_handler.fetch_specific_data(character_id)
    print("iron man", one_character_df)

    # Create a News API handler
    news_headlines_handler = HandlerFactory.get_handler('news', 'everything_samsung')
    headlines_df = news_headlines_handler.fetch_everything_samsung()
    print("samsung DataFrame", headlines_df)

    # Fetch hot topics
    news_hot_topic_handler = HandlerFactory.get_handler('news', 'top-headlines')
    hot_topics_df = news_hot_topic_handler.get_headline_news()
    print("Headlines DataFrame", hot_topics_df)

    # For Spotify
    category_handler = HandlerFactory.get_handler('spotify', 'category')
    category_handler.fetch_and_save_categories()

    new_release_handler = HandlerFactory.get_handler('spotify', 'new_release')
    new_release_handler.fetch_and_save_new_releases()

    top_tracks_handler = HandlerFactory.get_handler('spotify', 'top_tracks')
    top_tracks_handler.fetch_and_save_top_tracks(
        playlist_id="3fMbdgg4jU18AjLCKBhRSm")
    
    artist_handler = HandlerFactory.get_handler('spotify', 'artist')
    print("issue here")
    artist_handler.fetch_and_save_top_artists("Sabrina Carpenter")
    artist_handler.fetch_and_save_artists("Sabrina Carpenter")

    artists_handler = HandlerFactory.get_handler('spotify', 'artists')
    artist_names = ["Adele", "Ed Sheeran", "Taylor Swift", "Cynthia Erivo", "Isabel LaRosa", "Lorde", "Mitski",
                    "The Weeknd", "Måneskin", "The Neighbourhood"]
    artists_handler.fetch_and_save_artists(artist_names)

if __name__ == "__main__":
    main()
