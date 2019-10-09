"""
===============
author:Administrator
time:15:08
E-mail:1223607348@qq.com
===============
"""
import requests
# # 方式一
# class HttpRequest(object):
#     def __init__(self,url,data):
#         # 准备请求数据
#         self.url = url
#         self.data = data
#         # 发送请求
#         response = requests.post(url=self.url,data=self.data)
#         # 获取响应结果
#         res = response.text()
#         print(res)
# login = HttpRequest("http://test.lemonban.com/futureloan/mvc/api/member/login",
#                     {'mobilephone':'13302024220','pwd':'123456a'})


# 方式二
class HttpRequest(object):
    '''发送不需要记录cookie的请求'''
    def request(self,mothod,url,data,headers=None):
        # p判断请求方法
        mothod =mothod.lower()
        if mothod == 'post':
            return requests.post(url=url,data=data,headers=headers)
        elif mothod == 'get':
            return requests.get(url=url,params=data,headers=headers)
test = HttpRequest()
test.request('post','http://47.92.107.201:9090/distributer/distributer/login',
             {
                 'email': '1223607348@qq.com',
                 'password': '123456',
                 'imgCode': 'qhg1',
                 'uuidCode': 0.4093672450126622
             })

