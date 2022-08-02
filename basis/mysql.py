from sqlite3 import Cursor
import pymysql

db = pymysql.connect(
    host='172.16.2.231',
    user='root',
    port=3307,
    password='byxf#2021',
    database='rta'
)

cursor  = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print ("Database version : {} ".format(data))

cursor.execute("select * from warn_config limit 1")
data = cursor.fetchone()
print(data)


db.close()
