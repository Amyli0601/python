"""
===============
author:Administrator
time:13:39
E-mail:1223607348@qq.com
===============
"""
'''
requests模块发送post请求
方法：requests.post()
参数传递：用data接收数据
'''
import requests
# 第一步：准备请求数据
# 目标url地址
url = 'http://47.92.107.201:9090/distributer/distributer/login'
# 请求参数
data = {
    'email':'1223607348@qq.com',
    'password':'123456',
    'imgCode':'qhg1',
    'uuidCode':0.4093672450126622
}

# 第二步：发送请求
response = requests.post(url=url,data=data,json=None)
print(response)
# # 第三步：获取响应结果，返回结果为str格式
# # 方式一：text
# print(reponse.text)
# # 方式二：content.decode，返回结果为str格式
# print(reponse.content.decode('utf8'))
# 方式三：json()：数据才能使用该方法获取响应数据
# .json()方法可以将返回json格式的字符串转换为python对应的字典或者列表格式
print(response.json())

