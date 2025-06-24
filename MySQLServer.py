import mysql.connector
from mysql.connector import Error
import os

def setup_alx_book_store_from_sql_file():
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'your_username',
        'password': 'your_password'
    }

    sql_file_path = "alx_book_store.sql"

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )

        if connection.is_connected():
            cursor = connection.cursor()
            print("Successfully connected to MySQL server.")

            if os.path.exists(sql_file_path):
                with open(sql_file_path, 'r') as file:
                    sql_script_content = file.read()

                for result in cursor.execute(sql_script_content, multi=True):
                    pass

                connection.commit()
                print(f"SQL script '{sql_file_path}' executed successfully!")
                print("Database 'alx_book_store' and its tables are now set up!")

            else:
                print(f"Error: SQL file '{sql_file_path}' not found. Cannot set up the database and tables.")

    except Error as e:
        print(f"Error during database setup: {e}")
    finally:
        if cursor:
            cursor.close()
            print("MySQL cursor closed.")
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    setup_alx_book_store_from_sql_file()
