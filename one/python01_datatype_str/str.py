"""
===============
author:Administrator
time:11:13
E-mail:1223607348@qq.com
===============
"""
'''
字符串：
1.定义：单引号、双引号、三引号、str()内置函数

注意点：
1.空白字符 布尔值为True和空字符 布尔值为False

切片和下标取值
1.索引取值：从左到右，从0开始；从右到左，从-1开始
2.切片：[start_index:end_index:步长] 左闭右开

字符串常用方法：
1.join 字符串拼接
2.find 查找元素的位置
3.count 查找元素的个数
4.replace 替换字符
5.spilt 字符串切割
6.format 格式化输出
7.upper 将字母大写
8.lower 将字母小写
'''
# name = '可乐'
# age = str(16)
# print(name)
# print(age,type(age))

# str1 = ''
# str2 = ' '
# print(bool(str1))
# print(bool(str2))

# # 下标取值
# str1 = 'hello python'
# print(str1[0])
# # 切片
# print(str1[0:5])

str1 = 'amy'
# 1.join 字符串拼接
# res = str1.join('li')
res = str1.join(['A','B','C'])
print(res)
# 2.find 查找元素的位置:每次只能查找一个元素
str2 = 'hello python'
print(str2.find('h'))
# 3.count 查找元素的个数
print(str2.count('o'))
# 4.replace 替换指定字符
print(str2.replace('p','P'))
# 5.spilt 字符串切割,返回一个列表
print(str2.split('o'))
# 6.format 格式化输出
# 7.upper 将字母大写
print(str2.upper())
# 8.lower 将字母小写
print(str2.lower())