import mysql
import mysql.connector

__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx == None:
        __cnx = mysql.connector.connect(user='root', password='password',
                                      host='127.0.0.1',
                                      database='gs')
    return __cnx