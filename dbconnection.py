from multiprocessing import connection
import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Mysql@12345',
    auth_plugin='mysql_native_password',
    database = 'resturant'
)

myaccess = connection.cursor()

myaccess.execute('CREATE DATABASE if not exists resturant')   #Creating database

#Show all tables
# myaccess.execute('Show tables')
# allTables = myaccess.fetchall()
# for table in allTables:
#     print(table)
