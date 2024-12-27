import pymysql

def db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='lingkungan_sehat',
        cursorclass=pymysql.cursors.DictCursor
    )
