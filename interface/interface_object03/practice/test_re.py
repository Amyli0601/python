"""
===============
author:Administrator
time:15:27
E-mail:1223607348@qq.com
===============
"""
'''
正则表达式
'''
import re

# search:查找
phone = '17302024220'
#
data = "{'mobilephone':'#phone#','pwd':'#pwd#','regname':'#kk#'}"
def replace(data):
    #
    while re.search(r'#(.+?)#',data):
        res = re.search(r'#(.+?)#',data)
        rdata = res.group()
        key = res.group(1)
        # 通过key获取配置文件动态参数的值
        value = key
        # 替换
        data = data.replace(rdata,phone)
    return data




#
# res2 = re.search(r'#(\d.+?)h(.+?)#','ssdsds#1343ahfgfgf#1212')
# print(res2.group())
# print(res2.group(1))
# print(res2.group(2))