
import mysql.connector
import pandas as pd
import config

# Establish a connection to the database
conn = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    port=config.port,
    database="marvel_data",

)
csv_file_path = 'D:/GBD-internship/csv_files/Marvel_transformed_files/marvel_formatted_all_characters.csv'
df = pd.read_csv(csv_file_path)
cursor = conn.cursor()
table_name = 'marvel_all_character'
if conn.is_connected():
    print("Connected to MySQL database")
    # Create a cursor object
    cursor = conn.cursor()
    # Insert data into the existing table
    insert_query = f"""
    INSERT INTO {table_name} (name,thumbnail,resource_uri,comics,events,popularity,character_ids,data_pulled_time)
    VALUES ( %s,%s,%s,%s,%s,%s,%s,%s)
    """
    for i, row in df.iterrows():
        cursor.execute(insert_query, (
            row['name'],
            row['thumbnail'],
            row['resourceURI'],
            row['comics'],
            row['events'],
            row['popularity'],
            row['character_ids'],
            row['data_pulled_time']
        ))
# Commit the transaction
conn.commit()
print("Data inserted successfully")
