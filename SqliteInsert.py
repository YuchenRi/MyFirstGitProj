import sqlite3

sqliteConnection = sqlite3.connect('first_example.db')
print("Database connected")

Cursor = sqliteConnection.cursor()
print("Database initialized")

insertTable_query = """
INSERT INTO emp(name, address, contact, post) VALUES(" Anishma, Bardiya, 9812345745, Manager ") 
"""
Cursor.execute(insertTable_query)

insertTable_query = """
INSERT INTO emp(name, address, contact, post) VALUES(" Rima, Nawalparasi, 9812555175, CEO ") 
"""
Cursor.execute(insertTable_query)

insertTable_query = """
INSERT INTO emp(name, address, contact, post) VALUES(" Aashis, KTM, 9876349820, Programmer ") 
"""
Cursor.execute(insertTable_query)

