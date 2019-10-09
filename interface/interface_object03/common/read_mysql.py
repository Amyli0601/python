"""
===============
author:Administrator
time:14:58
E-mail:1223607348@qq.com
===============
"""
import pymysql
from interface_object03.common.read_config import myconf
class ReadSQL(object):
    '''操作数据库的类'''
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect(
                host=myconf.get('mysql','host'),   # 数据库地址
                port = myconf.getint('mysql','port'), # 端口
                user = myconf.get('mysql','user'),  # 账号
                password = myconf.get('mysql','password'),  # 密码
                database = myconf.get('mysql','database'), # 数据库名
                charset = 'utf8' # 指定编码格式
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


