from dbconnection import connection
myaccess = connection.cursor()

# myaccess.execute('Create table if not exists food_category (c_id int primary key, cate_name varchar(70))')

# Add category
# sql = 'INSERT INTO food_category (c_id, cate_name) VALUES (%s, %s)'
# val = (4, 'sweets')
# myaccess.execute(sql, val)
# connection.commit()
# print('category added')

#show all categories
myaccess.execute('Select * from food_category')
allData = myaccess.fetchall()
for raw in allData:
    print(raw)


# update category
# sql = 'update food_category SET cate_name = "veg" where c_id = 1'
# myaccess.execute(sql)
# connection.commit()
# print('data updated')


# Delete categories  
# myaccess.execute('delete from food_category where c_id = 4')
# connection.commit()
# print('raw deleted')

