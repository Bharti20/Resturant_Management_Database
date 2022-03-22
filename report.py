from dbconnection import connection
myaccess = connection.cursor()

# creating table 
# myaccess.execute('CREATE TABLE if not exists reports (rep_id int, item_name varchar(30), item_type varchar(20), massage varchar(255))')


# add report 
# sql = 'INSERT INTO reports (rep_id, item_name, item_type, massage) VALUES (%s, %s, %s, %s)'
# val = (2, 'rasmalai','sweets', 'It was not fresh')
# myaccess.execute(sql, val)
# connection.commit()


# show reports of all food item
myaccess.execute('select * from reports')
result = myaccess.fetchall()
for i in result:
    print(i)

