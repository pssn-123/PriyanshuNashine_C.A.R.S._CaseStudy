import mysql.connector as sql
from util.PropertyUtil import *


class DBConnection:
    conn = ''
    @staticmethod
    def getConnection():
        l = PropertyUtil.getPropertyString()
        conn = sql.connect(host=l[0], database=l[1], user=l[2], password=l[3])
        return conn
