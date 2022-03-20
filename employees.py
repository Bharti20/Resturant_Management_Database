from dbconnection import connection
myaccess = connection.cursor()

# Creating table
# myaccess.execute('CREATE TABLE Employees (emp_id int PRIMARY KEY, emp_name varchar(50) not null, dept_id int, address varchar(255), phone varchar(255) not null, parent_name varchar(50), spouse varchar(50))')

# Add data 
# sql = 'INSERT INTO Employees (emp_id,emp_name,dept_id,address,phone,parent_name,spouse) VALUES (%s, %s,%s,%s,%s,%s,%s)'
# val = (7,'mushkan', 4,'citymarket,Pune', '9732356786', 'Chhaya', '')
# myaccess.execute(sql, val)
# connection.commit()
# print('data added')


# Show all data 
myaccess.execute('Select * from Employees')
allData = myaccess.fetchall()
for raw in allData:
    print(raw)

# Update data 
# sql = 'update Employees SET address = "kashmir india" where dept_id = 1'
# myaccess.execute(sql)
# connection.commit()
# print('data updated')

# Delete Employee data 
# myaccess.execute('delete from Employees where emp_id = 7')
# connection.commit()
# print('raw deleted')


