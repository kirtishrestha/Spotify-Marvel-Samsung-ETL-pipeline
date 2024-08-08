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
    # my_cursor.execute("show databases")
    my_cursor.execute("select * from marvel_data.marvel_all_character")
    result = my_cursor.fetchall()
    for data in result:
        print(data)
