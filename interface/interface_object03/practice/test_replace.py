"""
===============
author:Administrator
time:14:39
E-mail:1223607348@qq.com
===============
"""
'''
封装一个替换数据的方法：
封装的需求：
1、替换用例中的参数
2、简化替换的流程

实现思路：
1、获取用例数据
2、判断该用例数据是否有需要替换的参数
3、对数据进行替换
'''
import re
from interface_object03.common.read_config import myconf
s = "{'mobilephone':'#phone#','pwd':'#pwd#','regname':'LL'}"
# 第一步：通过search进行匹配
# 第二步：判断是否匹配到数据
while re.search(r'#(.+?)#',s):
    res = re.search(r'#(.+?)#',s)
    # 获取匹配内容
    rdata = res.group()
    # 提取要替换的字段
    key = res.group(1)
    # 通过提取的字段，去配置文件中读取对应的数据内容
    phone = myconf.get('data',key)
    # 进行替换
    # print(rdata,phone)
    s = re.sub(rdata,phone,s)
print(s)
