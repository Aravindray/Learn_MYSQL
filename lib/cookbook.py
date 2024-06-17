'''lib file for connection mysql server'''
import mysql.connector

conn_params = {
    "host":"localhost",
    "database": "cookbook",
    "user": "cbuser",
    "password": "cbpass"
}

def connect():
    ''' return database connection '''
    return mysql.connector.connect(**conn_params)
