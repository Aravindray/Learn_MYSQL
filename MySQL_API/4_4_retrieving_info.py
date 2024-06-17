'''How it works -> connections object, connection return cursor object then cursor have execute method'''
'''conn -> cursor -> execute -> sql statement'''
import mysql.connector
import cookbook

# connect to server
conn = cookbook.connect()
cursor = conn.cursor()

# Statement which don't return result set

# If any modification by default it happens inside the transaction mode
cursor.execute("UPDATE profile SET cats = cats+1 WHERE name = 'Sybil'")
print(f'No of rows effected {cursor.rowcount}')

# to save the changes don't forget to commit it
conn.commit()

# close the cursor
cursor.close()

# Statement does return result set
# Method 1 - Using fetchone()

cursor = conn.cursor()
cursor.execute("SELECT id, name, cats FROM profile")
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(f'id: {row[0]}, name: {row[1]}, cats: {row[2]}')
print(f'No of rows returned {cursor.rowcount}')
cursor.close()

# Method 2 - Using cursor itself

cursor = conn.cursor()
cursor.execute('SELECT id, name, cats from profile')
for (id, name, cats) in cursor:
    print(f'id: {id}, name: {name}, cats: {cats}')
print(f'No of rows returned {cursor.rowcount}')
cursor.close()

# Method 3 - Using fetchall() - convenient way

cursor = conn.cursor()
cursor.execute('SELECT id, name, cats from profile')
rows = cursor.fetchall()
for row in rows:
    print(f'id: {row[0]}, name: {row[1]}, cats: {row[2]}')
print(f'No of returned {cursor.rowcount}')
print(rows)
print(rows[1][2]) # rows[col][rows]
cursor.close()
