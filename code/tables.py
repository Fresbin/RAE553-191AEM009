import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS types (name text, price real)"
cursor.execute(create_table)

cursor.execute("INSERT INTO types VALUES ('type1', 250)")

connection.commit()

connection.close()
