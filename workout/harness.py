import mysql.connector
import cookbook

try:
    conn = cookbook.connect()
    print('Connected')
except mysql.connector.Error as e:
    print('Cannot connect to server')
    print(f'Error Code: {e.errno}')
    print(f'Error Msg: {e.msg}')
else:
    conn.close()
    print('Disconnected')
