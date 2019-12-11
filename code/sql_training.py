import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password)"
cursor.execute(create_table)

users = {
        'user1': (1, 'fresbin', '1234'),
        'user2': (2, 'John', '2134'),
        'user3': (3, 'alex', '3567'),
        'user4': (4, 'freddy', '5763'),
        'user5': (5, 'emma', '9876')
        }
insert_query = ("INSERT INTO users VALUES (?, ?, ?)")
for user in users:
    cursor.execute(insert_query, users[user])
insert_query = ("SELECT * FROM users")
cursor.execute(insert_query)
myresult = cursor.fetchall()

for x in myresult:
  print(x)

cursor = connection.cursor()
connection.commit()
