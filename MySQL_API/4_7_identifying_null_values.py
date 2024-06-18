'''Identifying Null Values'''
import cookbook

conn = cookbook.connect()
cursor = conn.cursor()
cursor.execute("SELECT name, birth, foods FROM profile")

for row in cursor:
    row = list(row)
    for i, value in enumerate(row):
        if value is None:
            row[i] = 'NULL'
    print(f'name: {row[0]}, birth: {row[1]}, food: {row[2]}')
print(f'No of rows returned {cursor.rowcount}')
cursor.close()
