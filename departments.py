from dbconnection import connection
myaccess = connection.cursor()

#creating table 
# myaccess.execute('CREATE TABLE  if not exists Departments (dept_id int PRIMARY KEY, dept_name varchar(50) not null)')

# Add Department
# sql = 'INSERT INTO Departments (dept_id, dept_name) VALUES (%s, %s)'
# val = (4, 'Delivery Staff')
# myaccess.execute(sql, val)
# connection.commit()
# print('Department added')

#show all departments
myaccess.execute('select * from Departments')
data = myaccess.fetchall()
for raw in data:
    print(raw)

# update a department name
# sql = 'update Departments SET dept_name = "Managerial Staff" where dept_id = 1'
# myaccess.execute(sql)
# connection.commit()


# Delete a department 
# myaccess.execute('delete from Departments where dept_id = 4')
# connection.commit()
# print('raw deleted')


