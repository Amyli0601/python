"""
===============
author:Administrator
time:11:03
E-mail:1223607348@qq.com
===============
"""
'''
使用requests模块发送get请求
方法：requests.get()
参数传递：用params

'''
import requests

# 第一步：准备请求数据
url = 'http://47.92.107.201:9090/distributer/trade/product/100002'
# 准备请求头，字段格式
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
data = {'sessionId':'c02fabb8-c48c-4bd8-a80f-4490e26afc40'}
# 第二步：发送请求
response = requests.get(url=url,headers=headers,params=data)
print(response)
# 第三步：获取响应结果
print(response.json())
# 1、方式一：自动识别编码方式，对内容进行解码
# print(response.text)
# 2、方式二：指定解码方式
# print(response.content.decode('utf8'))