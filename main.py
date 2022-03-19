import mysql.connector

dbConnecion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Mysql@12345',
    auth_plugin='mysql_native_password',
    database = 'resturant'
)

myaccess = dbConnecion.cursor()

# myaccess.execute('CREATE DATABASE resturant')    #Creating database

#creating tables
# myaccess.execute('CREATE TABLE Departments (dept_id int PRIMARY KEY, dept_name varchar(50) not null)')
# myaccess.execute('CREATE TABLE Employees (emp_id int PRIMARY KEY, emp_name varchar(50) not null, dept_id int, address varchar(255), phone varchar(255) not null, parent_name varchar(50), spouse varchar(50))')
# myaccess.execute('Create table food_category (c_id int, cate_name varchar(70))')
# myaccess.execute('CREATE TABLE menu (item_id int, item_name varchar(50), price int, categ_id int)')
# myaccess.execute('CREATE TABLE customer_details(cus_id int primary key, cus_name varchar(50), phone varchar(20), address varchar(255))')
# myaccess.execute('CREATE TABLE odering_system (oder_sys_id int, oder_sys_name varchar(50))')
# myaccess.execute('CREATE TABLE oders (oder_id int, food_id int, item_quantity int, total_price int, oder_sys_id int)')

#Data insert 
# sql = 'INSERT INTO Departments (dept_id, dept_name) VALUES (%s, %s)'
# val = [(1753, 'Kitchen Staff'), (1, 'Managerial Staff'), (2, 'Floor Staff'), (3,'Bar Tenders'), (4, 'Delivery Staff')]
# myaccess.executemany(sql, val)
# dbConnecion.commit()

# sql = 'INSERT INTO Employees (emp_id,emp_name,dept_id,address,phone,parent_name,spouse) VALUES (%s, %s,%s,%s,%s,%s,%s)'
# val = [(1,'Bharti', 1,'kishanganj,Bihar', '9732456788', 'Mohan singh',''), (2,'Nikita', 2,'kishanganj,Bihar', '9732456776', '','Madan singh'), (3,'Rashid', 3,'Bhagalpur,Bihar', '9342456776', '', 'asma begam'), (4,'Alon', 5,'Huskur', '9877653123', 'Devid',''), (5,'Rosi', 4,'Sarjapur, Banglore', '9732356782', '','Champak'), (6,'Aples', 3,'Moroko', '3453356782', 'Mamta devi', ''), (7,'mushkan', 4,'citymarket,Pune', '9732356786', 'Chhaya', '')]
# myaccess.executemany(sql, val)
# dbConnecion.commit()

# sql = 'INSERT INTO food_category (c_id, cate_name) VALUES (%s, %s)'
# val = [(1,'veg'), (2, 'non veg'), (3, 'drinks'), (4, 'sweets')]
# myaccess.executemany(sql, val)
# dbConnecion.commit()

# sql = 'INSERT INTO menu (item_id, item_name, price, categ_id) VALUES (%s, %s,%s,%s)'
# val = [(1, 'Gobi manchurian', 100, 1),(2, 'Malai kofta', 90, 1),(3, 'paneer curry', 110, 1),(4, 'bhindi fry', 70, 1),(5, 'chiken fry', 120, 2),(6, 'fish curry', 150, 2),(7, 'egg curry', 60, 2),(8, 'mutton biryani', 170, 2), (9, 'lemon juice', 60, 3),(10, 'Pepsi', 70, 3),(11, 'soda', 50, 3),(12, 'gulab jamun', 40, 4),(13, 'Rasgula', 60, 4),(14, 'rasmali', 80, 4)]
# myaccess.executemany(sql, val)
# dbConnecion.commit()


# sql = 'INSERT INTO customer_details (cus_id, cus_name, phone, address) VALUES (%s, %s,%s,%s)'
# val = [(1, 'Sonam', '8976345212', 'citypark, Pune'),(2, 'Ankur', '9876456621', 'Gurgaon,Haryana'),(3, 'Nilesh', '1567890322', 'purnea,Bihar'),(4, 'Pravin', '7065443789', 'Kishanganj,Bihar'),(5, 'Ravina', '878956789','Ahmadabad'),(6, 'Sarmistha', '985345678', 'Kolkata'),(8, 'Kritika', '6045678922', 'delhi')]
# myaccess.executemany(sql, val)
# dbConnecion.commit()

# sql = 'INSERT INTO odering_system (oder_sys_id, oder_sys_name) VALUES (%s, %s)'
# val = [(1, 'offline'), (2, 'online'), (3, 'through_call')]
# myaccess.executemany(sql, val)
# dbConnecion.commit()

# sql = 'INSERT INTO oders (oder_id, food_id, item_quantity,total_price, oder_sys_id) VALUES (%s, %s,%s, %s,%s)'
# val = (3, 14,2, 160, 2 )
# myaccess.execute(sql, val)
# dbConnecion.commit()









# myaccess.execute('select * from Departments')
# result = myaccess.fetchall()
# for i in result:
#     print(i)
