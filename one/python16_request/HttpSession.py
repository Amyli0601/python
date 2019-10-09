"""
===============
author:Administrator
time:14:47
E-mail:1223607348@qq.com
===============
"""
from requests import session
# 方式一：
s = session()
class HttpSession(object):
    def __init__(self,url,data):
        # 准备请求数据
        self.url = url
        self.data = data
        response = s.post(url=self.url,data=self.data)
        # 获取响应结果
        res = response.json()
        print(res,type(res))
login = HttpSession("http://47.92.107.201:9090/distributer/distributer/login",
                    {"'email':'1223607348@qq.com','imgCode':'qhg1','password':'123456','uuidCode':'0.4093672450126622'"})




