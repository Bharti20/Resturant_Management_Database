from dbconnection import connection
myaccess = connection.cursor()

# myaccess.execute('CREATE TABLE customer_details(cus_id int primary key, cus_name varchar(50), phone varchar(20), address varchar(255))')


# sql = 'INSERT INTO customer_details (cus_id, cus_name, phone, address) VALUES (%s,%s,%s)'
# val = (6, 'Kritika', '6045678922', 'manali,house no 12, Banglore)
# myaccess.execute(sql, val)
# connection.commit() 


# show all customers details
myaccess.execute('select * from customer_details ')
allData = myaccess.fetchall()
for raw in allData:
    print(raw)


# update customer details
# sql = 'update customer_details set cus_name = "Bharti" where cus_id = 1 '
# myaccess.execute(sql)
# connection.commit()


# Delete item   
# myaccess.execute('delete from customer_details where cus_id = 6')
# connection.commit()
# print('raw deleted')


