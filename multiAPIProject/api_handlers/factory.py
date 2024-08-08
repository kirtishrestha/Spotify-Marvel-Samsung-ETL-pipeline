from Spotify.artist import ArtistsHandler
from Spotify.category import CategoryHandler
from Spotify.new_release import NewReleaseHandler
from Spotify.tracks import TopTracksHandler
from marvel.all_characters import AllCharactersHandler
from marvel.characters_by_id import OneCharacterHandler
from news.everything import LatestSamsungNews
# from pythonProject.multiAPIProject.api_handlers.news.everything import LatestSamsungNews
from news.headline_news import HeadlineNews


class HandlerFactory:
    @staticmethod
    def get_handler(api_type, handler_type):
        if api_type == 'marvel':
            if handler_type == 'all_characters':
                return AllCharactersHandler()
            elif handler_type == 'one_character':
                return OneCharacterHandler()
            # Add other Marvel handlers here
            else:
                raise ValueError(f"Unknown Marvel handler type: {handler_type}")
            
        elif api_type == 'news':
            if handler_type == 'everything_samsung':
                return LatestSamsungNews()
            elif handler_type == 'top-headlines':
                return HeadlineNews()
            else:
                raise ValueError(f"Unknown News handler type: {handler_type}")
            
        elif api_type == 'spotify':
            if handler_type == 'category':
                print("category")
                return CategoryHandler()
            elif handler_type == 'new_release':
                print("new release")
                return NewReleaseHandler()
            elif handler_type == 'top_tracks':
                print("top tracks")
                return TopTracksHandler()
            elif handler_type == 'artist':
                print("artist")
                return ArtistsHandler()
            elif handler_type == 'artists':
                print("artists")
                return TopTracksHandler()
            # Add other Spotify handlers here
            else:
                raise ValueError(f"Unknown Spotify handler type: {handler_type}")
            
        else:
            raise ValueError(f"Unknown API type: {api_type}")

if __name__ == '__main__':
    # Test HandlerFactory functionality
    try:
        marvel_handler = HandlerFactory.get_handler('marvel', 'all_characters')
        print("Marvel Handler Created:", type(marvel_handler))

        news_handler = HandlerFactory.get_handler('news', 'everything_samsung')
        print("News Handler Created:", type(news_handler))

        spotify_handler = HandlerFactory.get_handler('spotify', 'new_release')
        print("Spotify Handler Created:", type(spotify_handler))

    except Exception as e:
        print("Error during handler creation:", str(e))