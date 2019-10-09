"""
===============
author:Administrator
time:11:07
E-mail:1223607348@qq.com
===============
"""
import random

# 随机生成手机号
def random_phone():
    # 随机生成手机号的类
    phone = '13'
    for i in range(9):
        num = random.randint(1,9)
        phone+=str(num)
    return phone