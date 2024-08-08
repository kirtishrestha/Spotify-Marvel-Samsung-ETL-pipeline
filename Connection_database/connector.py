import mysql.connector
# import config

# Establish a connection to the database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    port="3306",
    database="Spotify"

)
if conn.is_connected():
    print("database connected")
    my_cursor = conn.cursor()
    # my_cursor.execute("show databases")
    my_cursor.execute("SELECT * FROM books")
    result = my_cursor.fetchall()
    for data in result:
        print(data)