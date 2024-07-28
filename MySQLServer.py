import mysql.connector
from mysql.connector import Error

def create_database(alx_book_store):
    try:
        # Establish the connection to the mySQL server
        connection = mysql.connector.connect(
            host = "",
            user = "",
            password = "",
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database alx_book_store created successfully!")

    except Error as e:
        print(f"Error {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database                        