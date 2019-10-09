"""
===============
author:Administrator
time:14:58
E-mail:1223607348@qq.com
===============
"""
import psycopg2
from interface.common.read_config import myconf
class ReadSQL(object):
    '''操作数据库的类'''
    def __init__(self):
        # 建立连接
        self.conn = psycopg2.connect(
                host=myconf.get('postgresql','host'),   # 数据库地址
                port = myconf.getint('postgresql','port'), # 端口
                user = myconf.get('postgresql','user'),  # 账号
                password = myconf.get('postgresql','password'),  # 密码
                database = myconf.get('postgresql','database') # 数据库名
                )
        # 创建一个游标
        self.cur = self.conn.cursor()
    def close(self):
        # 关闭游标，断开连接
        self.cur.close()
        self.conn.close()
    def fetchone(self,sql):
        # 查询一条数据
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()
    def fetchall(self,sql):
        # 返回sql语句查询到的所有数据
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()
    def find_count(self,sql):
        # 查询数据条数
        self.conn.commit()
        count = self.cur.execute(sql)
        return count


