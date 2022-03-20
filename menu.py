from dbconnection import connection
myaccess = connection.cursor()

# myaccess.execute('CREATE TABLE menu (item_id int primary key, item_name varchar(50), price int, categ_id int)')

# Add food item 
# sql = 'INSERT INTO menu (item_id, item_name, price, categ_id) VALUES (%s, %s,%s,%s)'
# val = (14, 'rasmalai', 80, 4)
# myaccess.execute(sql, val)
# connection.commit()

# show all items 
myaccess.execute('Select * from menu')
allData = myaccess.fetchall()
for raw in allData:
    print(raw)


# update menu
# sql = 'update menu SET price = "110" where item_id = 1'
# myaccess.execute(sql)
# connection.commit()
# print('data updated')


# Delete item   
# myaccess.execute('delete from menu where item_id = 14')
# connection.commit()
# print('raw deleted')
