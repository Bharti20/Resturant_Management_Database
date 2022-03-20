from dbconnection import connection
myaccess = connection.cursor()

# myaccess.execute('CREATE TABLE orders (customer_id int, food_id int, item_quantity int, total_price int, oder_sys_id int)')

#Add order
# sql = 'INSERT INTO orders (customer_id, food_id, item_quantity,total_price, oder_sys_id) VALUES (%s, %s,%s, %s,%s)'
# val = (4, 13,2, 120, 2 )
# myaccess.execute(sql, val)
# connection.commit()

# show all orders 
myaccess.execute('Select * from orders')
allData = myaccess.fetchall()
for raw in allData:
    print(raw)


# Update oders
# sql = 'update orders SET total_price = "200" where customer_id = 1'
# myaccess.execute(sql)
# connection.commit()
# print('data updated')


# Delete item   
# myaccess.execute('delete from orders where customer_id = 4')
# connection.commit()
# print('raw deleted')


# show data with customer name
# sql = 'select  orders.customer_id, customer_details.cus_name, orders.total_price from orders inner join customer_details on customer_details.cus_id = orders.customer_id'
# myaccess.execute(sql)
# allData = myaccess.fetchall()
# for i in allData:
#     print(i)




