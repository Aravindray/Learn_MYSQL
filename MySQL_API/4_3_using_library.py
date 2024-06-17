import cookbook
import mysql.connector
import sys

try:
    conn = cookbook.connect()
    print('Connected')
except mysql.connector.Error as e:
    print('Cannot connect to server')
    print(f'Error Code: {e.errno}')
    print(f'Error Msg: {e.msg}')
    print(f'Error SQLSTATE: {e.sqlstate}')
else:
    conn.close()
    print('Disconnected')

print(f'Python look for its modules under these paths:\n {sys.path}')
