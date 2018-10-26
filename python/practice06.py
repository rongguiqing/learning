import mysql.connector

conn = mysql.connector.connect(user="root", password="rong1987", database="test")
cursor = conn.cursor()
cursor.execute('create table user if(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['12', 'Jack'])
print('rowcount=',cursor.rowcount)
conn.commit()
conn.close()