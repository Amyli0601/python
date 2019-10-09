"""
===============
author:Administrator
time:14:58
E-mail:1223607348@qq.com
===============
"""
'''
为什么要封装?
方便使用
封装的需求是什么?
逻辑代码封装成方法，关键数据参数化处理
'''
import pymysql
class ReadSQL(object):
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect(host='test.lemonban.com',   # 数据库地址
                port = 3306, # 端口
                user = 'test',  # 账号
                password = 'test',  # 密码
                database = 'future',    # 数据库名
                )
        # 创建一个游标
        self.cur = self.conn.cursor()
    def close(self):
        # 关闭游标，断开连接
        self.cur.close()
        self.conn.close()
    def fetchone(self,sql):
        # 查询一条数据
        self.cur.execute(sql)
        return self.cur.fetchone()
    def fetchall(self,sql):
        # 返回sql语句查询到的所有数据
        self.cur.execute(sql)
        return self.cur.fetchall()
    def find_count(self,sql):
        # 查询数据条数
        count = self.cur.execute()
        return count
if __name__=='__main__':
    sql1 = 'select * from member where MobilePhone="18999990252"'
    sql2 = "select * from member LIMIT 5;"
    db = ReadSQL()
    res1 = db.fetchone(sql1)
    res2 = db.fetchall(sql2)
    print(res1,res2)