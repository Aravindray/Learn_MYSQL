import mysql.connector

conn_params = {
    "host":"localhost",
    "database": "cookbook",
    "user": "cbuser",
    "password": "cbpass"
}

def connect():
    return mysql.connector.connect(**conn_params)
