import mysql.connector
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password")
    if conn.is_connected():
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()
except mysql.connector.Error as e:
    print(f"Connection error: {e}")
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("MySQL connection is closed")
