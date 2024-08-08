import mysql.connector
import config

# Establish a connection to the database
conn = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    port=config.port,
    database="marvel_data"

)
if conn.is_connected():
    print("database connected")
    my_cursor = conn.cursor()
    # create a table if not exist
    create_table = f"""
           create table IF NOT EXISTS marvel_all_character_data(
           id INT AUTO_INCREMENT PRIMARY KEY,
           name VARCHAR(25),
           thumbnail VARCHAR(50),
           resource_uri VARCHAR(25),
           comics int,
           events int,
           popularity enum("high","medium","low"),
           character_ids int,
           data_pulled_time datetime
           )
           """
    my_cursor.execute(create_table)
    my_cursor.close()
    conn.close()
else:
    print("connection error")
