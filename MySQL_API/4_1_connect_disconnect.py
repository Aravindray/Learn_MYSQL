'''Connect to the server and select the database and disconnect from the server'''
import mysql.connector

try:
    conn = mysql.connector.connect(
        database = 'cookbook',
        host = 'localhost',
        user = 'cbuser',
        password = 'cbpass'
    )
    print('Connected')
except:
    print('Cannot connect to server')
else:
    conn.close()
    print('Disconnected')

# Another way to connect to the database

conn_params = {
    "host": "localhost",
    "database": "cookbook",
    "user": "cbuser",
    "password": "cbpass"
}
conn_new = mysql.connector.connect(**conn_params)
print('Connected')
