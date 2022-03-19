import mysql.connector

dbConnecion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Mysql@12345',
    auth_plugin='mysql_native_password',
    database = 'resturant'
)

myaccess = dbConnecion.cursor()

# myaccess.execute('CREATE DATABASE resturant')

myaccess.execute('CREATE TABLE Departments (dept_id int PRIMARY KEY, dept_name varchar(50) not null)')
myaccess.execute('CREATE TABLE Departments (dept_id int PRIMARY KEY, dept_name varchar(50) not null)')


