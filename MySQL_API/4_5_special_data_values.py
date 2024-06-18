'''Handling special characters and NULL values is important and it also prevent sql injection attack'''
import mysql.connector
import cookbook

# Connecting to server
conn = cookbook.connect()
cursor = conn.cursor()

# Using Placeholder
cursor.execute("INSERT INTO profile (name, birth, color, foods, cats) VALUES (%s, %s, %s, %s, %s)", ("De'mont", '1973-01-12', None, "eggroll", 4))

cursor.close()
conn.commit()

# To bind single value - method 1

cursor = conn.cursor()
cursor.execute("SELECT id, name, cats FROM profile WHERE cats = %s", (3,))
for (id, name, cats) in cursor:
    print(f'id: {id}, name: {name}, cats: {cats}')
print(f'No of rows returned {cursor.rowcount}')
cursor.close()

# To bind single value - method 2

cursor = conn.cursor()
cursor.execute("SELECT id, name, cats FROM profile WHERE cats = %s", [4])
for (id, name, cats) in cursor:
    print(f'id: {id}, name: {name}, cats: {cats}')
print(f'No of rows returned {cursor.rowcount}')
cursor.close()
