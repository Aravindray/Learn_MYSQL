'''Handling Error Basis'''
import mysql.connector

conn_params = {
    "host": "localhost",
    "user": "baduser",
    "password": "badpass",
    "database": "cookbook"
}

try:
    conn = mysql.connector.connect(**conn_params)
    print('Connected')
except mysql.connector.Error as e:
    print('Cannot connect to server')
    print(f'Error Code {e.errno}')
    print(f'Error Msg: {e.msg}')
    print(f'Error SQLSTATE: {e.sqlstate}')
