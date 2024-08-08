import pandas as pd

from news.news_handler import NewsHandler


# from news.news_handler import NewsHandler


class LatestSamsungNews(NewsHandler):

    def fetch_everything_samsung(self):
        endpoint = 'everything'
        response_url = self.make_request(endpoint)
        print("response url", response_url)
        samsung_articles = []
        for item in response_url['articles']:
            source = item['source']['name']
            author = item['author']
            title = item['title']
            description = item['description']
            url = item['url']
            publishedAt = item['publishedAt']
            samsung_articles.append(
                [source, author, title, description, url, publishedAt])

        df = pd.DataFrame(samsung_articles,
                          columns=['Source', 'Author', 'Title', 'Description', 'URL', 'publishedAt'])
        print(df)
        # df.to_csv('api_handlers/news/news_csv_files/samsung_articles.csv', index=False)
        # df.to_csv('D:/GBD-internship/csv_files/news_raw_data/samsung_articles.csv', index=False)
        df.to_csv('../multiAPIProject/csv_files/marvel_news_csv_files/samsung_articles.csv', index=False)

        print("Data has been written to samsung_articles.csv")
