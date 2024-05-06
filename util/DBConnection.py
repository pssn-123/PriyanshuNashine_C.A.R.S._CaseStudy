import mysql.connector as sql
from util.PropertyUtil import *

"""conn = sql.connect(host='localhost', database = 'CARS', user = 'root', password = 'Priyanshu2003')
if conn.is_connected:
    print("The database is connected")
stmt = conn.cursor()
stmt.execute('create table Examp(id int primary key auto_increment, ')
print(stmt.fetchall())
"""
class DBConnection:

    @staticmethod
    def getConnection():
        l = PropertyUtil.getPropertyString()
        conn = sql.connect(host=l[0], database=l[1], user=l[2], password=l[3])
        return conn