import mysql.connector
conn = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "password")
if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    cursor.close()
    conn.close()
else:
    print("Error: Failed to connect to MySQL server")

