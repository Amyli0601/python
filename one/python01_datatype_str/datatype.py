"""
===============
author:Administrator
time:15:19
E-mail:1223607348@qq.com
===============
"""
'''
标识符：有数字、字母、下划线组成，不能以数字开头，不能使用关键字
1.print
在python2中是关键字，
在python3中是内置函数（不建议使用print作为标识符）

数值类型
1.整数 int
2.浮点数 float小数
3.
'''
# print('*'*20)
# # 算数运算符
# a = 100
# b = 2
# c = 30
# # //向下取整
# print(a//c)
# # %取余
# print(a%c)
# # **幂运算
# print(a**b)

# 赋值运算符
# # +=
# a += c
# print(a)
# # -=
# a -= 2
# print(a)
# # /=
# a /= b
# print(a)

# 比较运算符
# < > <= >= != ==条件成立返回True;不成立返回False
# print(100==1)
# # 逻辑运算符 优先级
# a = 100
# b = 2
# c = 30
# # or 只要有一个条件成立就返回True;否则，返回False
# print(a > 50 or b > 50)
# # and 条件都成立就返回True;否则，返回False
# print(a > 50 and b > 50)
# # not 如果条件返回True，not之后返回False
# print(not a > 50 or b > 50)

# # 成员运算符
# # in   ont in 条件成立返回True，否则返回False
# str1 = 'adafd7ta'
# print('a' in str1)
# print('ab' in str1)

# # 身份运算符 小整数池：-5 到 256 交互环境和python内返回结果不一致
# # is   is not
# a = 100
# b = 1000
# c = 100
# d = 1000
# print(a is b)
# print(a is c)
# print(b is d)

'''
random模块：生成随机数
'''
import random
# 1.随机生成0-1的随机浮点数
a = random.random()
print(a)
# 2.随机生成随机整数
b = random.randint(1,20)
print(b)













