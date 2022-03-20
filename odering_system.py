from dbconnection import connection
myaccess = connection.cursor()

# myaccess.execute('CREATE TABLE odering_system (oder_sys_id int, oder_sys_name varchar(50))')

# Add more option
# sql = 'INSERT INTO odering_system (oder_sys_id, oder_sys_name) VALUES (%s, %s)'
# val = (3, 'through_call')
# myaccess.execute(sql, val)
# connection.commit()

# show all items 
myaccess.execute('Select * from odering_system')
allData = myaccess.fetchall()
for raw in allData:
    print(raw)

#update system 
# sql = 'update odering_system SET oder_sys_name = "offline" where oder_sys_id = 1'
# myaccess.execute(sql)
# connection.commit()
# print('data updated')


# Delete item   
# myaccess.execute('delete from odering_system where oder_sys_id = 3')
# connection.commit()
# print('raw deleted')
