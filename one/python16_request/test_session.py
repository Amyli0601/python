"""
===============
author:Administrator
time:14:37
E-mail:1223607348@qq.com
===============
"""
'''
session对象发送请求的作用：记录上一次请求的cookie信息来进行鉴权

'''
from requests import session

# 创建session对象
s = session()
# 访问登录接口
# 准备登录数据
url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
data = {
    'mobilephone':'13302024220',
    'pwd':'',
}
# 发送登录请求
response1 = s.post(url=url,data=data)
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
response = s.post(url=url1,data=data1)

# # 第三步：获取响应结果，返回结果为str格式
res = response.json()
print(res)