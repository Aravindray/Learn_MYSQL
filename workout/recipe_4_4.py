# Retrieve values from database
import cookbook

conn = cookbook.connect()

cursor = conn.cursor()
# cursor.execute("UPDATE profile SET cats = cats+1 WHERE name = 'Sybil'")
# print(f"No of rows updated: {cursor.rowcount}")
# conn.commit()

''' cursor.execute("SELECT id, name, cats FROM profile")
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(f'id: {row[0]}, name: {row[1]}, cats: {row[2]}')
print(f'No of rows returned {cursor.rowcount}') '''

cursor.execute('SELECT id, name, cats FROM profile')

# for (id, name, cats) in cursor:
#     print(f'id: {id}, name: {name}, cats: {cats}')
# print(f'No of rows returned {cursor.rowcount}')

rows = cursor.fetchall()

for row in rows:
    print(f'id: {row[0]}, name: {row[1]}, cats: {row[2]}')
print(f'No of rows returned {cursor.rowcount}')
cursor.close()
