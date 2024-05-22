import sqlite3

sqliteConnection = sqlite3.connect('first_example.db')
print("Database connected")

Cursor = sqliteConnection.cursor()
print("Database initialized")

createTable_query = """
CREATE TABLE IF NOT EXITS emp (id integer primary key AUTOINCREMENT, name text, address text, contact integer, Post integer)
"""
Cursor.execute(createTable_query)