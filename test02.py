"""
===============
author:Administrator
time:11:31
E-mail:1223607348@qq.com
===============
"""
#a = int (input('请输入整数：'))
#if (a % 2) ==0:
#   print("偶数")
#else:
#   print("奇数")


# b =float(input("请输入橘子的价格："))
# import random
# print(b*random.randint(5,10))


# c = ['hello','python18','!']
# print','.join(c)
#
#
# d = 'python hello aaa 123123aabb'
# print('字符串中a的个数：',d.count("a"))



#f = 'python hello aaa 123123aabb'
#print("符串中'123'的下标起始位置:",f.find('123'))


# g = 'python hello aaa 123123aabb'
# if 'o a' in g:
#     print('是')
# else:
#     print('否')
# if 'he' in g:
#     print('是')
# else:
#     print('否')
# if 'ab' in g:
#     print('是')
# else:
#     print('否')

# # def fun(tt):
#     g = 'python hello aaa 123123aabb'
#     if tt in g:
#         print('是')
#     else:
#         print('否')
# list = ['o a','he','ab']
# for tt in list:
#     fun(tt)
#


import random
orange = random.randint(5,10)

while True:
    price = float(input("请输入橘子价格:"))
    if price <= 0:
        continue
    else:
        number = price * orange
        print("总价:", number)
        break







