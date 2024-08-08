import pandas as pd
import os
from datetime import datetime

print(os.getcwd())
file_path = 'D:/GBD-internship/csv_files/news_raw_data/samsung_articles.csv'
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    print('file found')
    df = pd.read_csv(file_path)
    # a new column 'popularity' based on comics appearances
    article_counts = df.groupby('Source').size().reset_index(name='Article Count')
    print(article_counts)
    unique_authors = df.groupby('Source')['Author'].nunique().reset_index(name='Unique Authors')
    authors_list = df.groupby('Source')['Author'].apply(list).reset_index(name='Authors')
    articles_per_author = df.groupby('Author').size().reset_index(name='Article Count')
    articles_per_source_author = df.groupby(['Source', 'Author']).size().reset_index(name='Article Count')
    most_frequent_author = df.groupby('Source')['Author'].agg(lambda x: x.value_counts().index[1]).reset_index(
        name='Most Frequent Author')
    article_count_per_author_source = df.groupby(['Source', 'Author']).size().unstack(fill_value=0)
    merged_df = article_counts.merge(unique_authors, on='Source') \
        .merge(authors_list, on='Source') \
        .merge(most_frequent_author, on='Source')
    # Get the current date and time
    current_datetime = datetime.now()
    merged_df['data_pulled_time'] = current_datetime
    # df.to_csv('../marvel_csv_files/marvel_formatted_all_characters.csv', index=False)
    merged_df.to_csv('../../../csv_files/marvel_news_csv_files/samsung_data_transformed.csv', index=False)
    print("saved in file")
