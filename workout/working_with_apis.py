import mysql.connector

conn_param = {
    "host": "localhost",
    "database": "cookbook",
    "user": "baduser",
    "password": "badpassword"
}

try:
    conn = mysql.connector.connect(**conn_param)
    print('Connected')
except mysql.connector.Error as e:
    print('Cannot connect to server')
    print(f"Error code: {e.errno}")
    print(f"Error message: {e.msg}")
    print(f"Error SQLSTATE: {e.sqlstate}")
else:
    conn.close()
    print('Disconnected')
