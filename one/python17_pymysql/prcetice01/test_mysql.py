"""
===============
author:Administrator
time:14:16
E-mail:1223607348@qq.com
===============
"""
'''
数据库地址：test.lemonban.com
端口：3306
账号：test
密码：test


'''
import pymysql
# 第一步：连接到数据库，创建游标
conn = pymysql.connect(host='test.lemonban.com',   # 数据库地址
                port = 3306, # 端口
                user = 'test',  # 账号
                password = 'test',  # 密码
                database = 'future',    # 数据库名
                )
cur = conn.cursor()
# 第二步：执行sql语句
sql1 = 'select * from member where MobilePhone="18999990252"'
sql2 = "select * from member LIMIT 5;"

res1 = cur.execute(sql1)
res2 = cur.execute(sql2)
print(res1,res2)
# 第三步：获取结果
# 获取查询集的第一条数据
data1 = cur.fetchone()
print(data1)
# 获取查询集的所有数据
data2 = cur.fetchall()
for i in data2:
    print(i)

# 执行增加、修改、删除的语句,执行完提交才会生效
conn.commit()








