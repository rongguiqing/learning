import mysql.connector

conn = mysql.connector.connect(user="root", password="rong1987", database="test")
'''
cursor = conn.cursor()
cursor.execute('create table users (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into users (id, name) values (%s, %s)', ['12', 'Jack'])
print('rowcount=',cursor.rowcount)
conn.commit()
conn.close()
'''
cursor = conn.cursor()
cursor.execute('select * from users where id = %s', ('12',))
value = cursor.fetchall()
print(value)
cursor.close()
conn.close()
