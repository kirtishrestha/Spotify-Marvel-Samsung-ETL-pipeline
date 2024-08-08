import pandas as pd

from news.news_handler import NewsHandler


# from news.news_handler import NewsHandler


class HeadlineNews(NewsHandler):
    def get_headline_news(self):
        endpoint = 'top-headlines'
        response_url = self.make_request(endpoint)
        top_headlines_technology = []
        for items in response_url['articles']:
            source_name = items['source']['name']
            author = items['author']
            title = items['title']
            description = items['description']
            url = items['url']
            publishedAt = items['publishedAt']
            content = items['content']
            top_headlines_technology.append([source_name, author, title, description, url, publishedAt, content])

        df = pd.DataFrame(top_headlines_technology,
                          columns=['Source_name', 'Author', 'Title', 'Description', 'URL', 'PublishedAt',
                                   'Content'])

        print(df)
        # df.to_csv('D:/GBD-internship/csv_files/news_raw_data/top_headlines_technology.csv', index=False)
        df.to_csv('../multiAPIProject/csv_files/marvel_news_csv_files/top_headlines_technology.csv', index=False)

        print("Data has been written to top_headlines_technology.csv")
