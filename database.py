import mysql.connector
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kakarot",
        database="nayepankh"
    )
    return connection