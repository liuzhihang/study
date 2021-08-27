#!/usr/bin/python3

import pymysql

# 打开数据库连接
connect = pymysql.connect(host='localhost', user='root', database='demo')

# 使用 cursor() 方法创建一个游标对象 cursor

cursor = connect.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select * from trans_order where id = 1;")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print(f"当前数据是 :  {data}")

# 关闭数据库连接
connect.close()
