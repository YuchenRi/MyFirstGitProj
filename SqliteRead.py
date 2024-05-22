import sqlite3

sqliteConnection = sqlite3.connect('first_example.db')
print("Database connected")

Cursor = sqliteConnection.cursor()
print("Database initialized")

sqlRead_query = "SELECT * FROM emp;"
Cursor.execute(sqlRead_query)
print(Cursor.fetchall())

sqliteConnection.close()