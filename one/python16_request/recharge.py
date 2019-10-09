"""
===============
author:Administrator
time:14:05
E-mail:1223607348@qq.com
===============
"""
'''
如何访问需要鉴权的接口
案例
充值接口：需要在登录的情况下才能访问

'''
import requests
# 访问登录接口
# 准备登录数据
url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
data = {
    'mobilephone':'13302024220',
    'pwd':'123456a',
}
# 发送登录请求
response1 = requests.post(url=url,data=data)
# 打印登录结果
print(response1.json())



# 第一步：准备请求数据
# 目标url地址
url1 = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
# 请求参数
data1 = {
    'mobilephone':'13302024220',
    'amount':2000
}

# 第二步：发送请求
response = requests.post(url=url1,data=data1)

# # 第三步：获取响应结果，返回结果为str格式
res = response.json()
print(res)

'''
使用requests先进行登录，然后再充值，还是没有权限的原因：
http请求是无状态的，上一次请求的请求状态，下一次请求是无法获取的（两个请求完全独立）
解决方法：使用session对象发送请求
'''