"""
===============
author:Administrator
time:17:52
E-mail:1223607348@qq.com
===============
"""
# a = 1,
# while a<7:
#     if (a%2==0):
#         print(a,'is even')
#     else:
#         print(a,'is odd')
#     a+=1
#

# a = 'saudiah'
# print(type(a))
#
# import keyword
# print(keyword.kwlist)
#
#
# desc = '这个是用来\
# 测试换行的\
# 额'
# print(desc)
#
# name = input('请输入姓名:')
# age = input('请输入年龄：')
# print('名字:',name,"\n"'年龄:',age)

# print("学号\t    姓名\t语文\t数学\t英语")
# print("2017001\t曹操\t99\t88\t0")
# print("2017002\t周瑜\t92\t45\t93")
# print("2017008\t黄盖\t77\t82\t100")

# 算术运算符
# a = 100
# b = 3
# print(a//b)

# 赋值运算符= += -= *= /=
# c = 100
# c +=3
# print(c)

# 比较运算符< > <= >= != ==条件成立返回True，否则返回False
# a = 10
# b = 20
# print(a!=b)

# 逻辑运算符or and not
# a = 100
# b =10
# c = 50
# print(a>b and not b>c)

# 成员运算符 in not in
# str1 = 'adagidya'
# print('a' in str1)
# print('ai' in str1)

# 身份运算符is is not 在交互环境运行结果才是正确的
# a = 1000
# b = 1000
# c = a
# print(b is a)
# print(a is c)

# 空字符和空白字符
# a = ''
# b = ' '
# print(a==b)

# 字符串：下标索引取值和切片
# 索引：从左往右，从0开始，从右往左，从-1开始
# a = 'asdfghjkl'
# print(a[1])
#
# 切片:[start_index：end_index:步长]，左闭右开
# 起始位置不填默认从0开始，终止位置不填默认取到最末尾
# str1 ='hello python'
# print(str1[::2])

# 字符串拼接
# str1 = 'aabbcc'
# str2 = 'ddeeff'
# print(str1+str2)

# 换行符\n
# str1 = 'hello\npython'
# print(str1)
# 制表符\t 表示四个空格键
# str1 = 'hello\tpython'
# print(str1)
# 去除转义
# str1 = r'hello\npython'
# print(str1)

# 字符串常用方法
# 1、拼接join
# a = 'aabbcc'
# str1 = a.join(['11','22','33'])
# str2 = ' '.join('123')
# print(str2)
# 2、find 通过字符查询下标位置
# 如果找到多个返回第一个字符的下标位置，找不到返回-1
# str1 = 'hello python'
# print(str1.find('py'))
# 3、count 统计元素的个数
# str1 = 'hello python'
# print(str1.count('o'))
# 4、replace 指定字符替换
# str1 = 'abc123acdvjs'
# print(str1.replace('a','A').replace('b','B'))
# 5、split 指定字符分割
# str1 = 'abc 123 ac  dv  js'
# print(str1.split(' '))
# 6、upper 将字母大写
# str1 = 'abc 123 ac  dv  js'
# print(str1.upper())
# 7、lower 将字母小写
# 8、格式化输出
# format {}占位
# str1 = '今收到{: ^4s},交来学费{:.2f},日期{}'
# print(str1.format('测试',8000,'2019-07-31'))
# str2 = '今天{}，我准备去{}，预计要花{:.2f}元'.format('2019-08-01','日本',10000)
# print(str2)
# str3 = '{a}xxx{b:.2f}yyy{c}'.format(a=100,b=200,c=300)
# print(str3)
# 传统的格式化输出：%占位 %s:占位字符串 %d:占位数值类型
# str1 = '今天%s，我准备去%s，预计要花%.2f元'%('2019-08-01','日本',10000.00)
# print(str1)

# if 条件判断
# score = float(input('请输入您的考试成绩：'))
# if score>=90:
#     print('您的考试成绩为：A')
# elif score>=80:
#     print('您的考试成绩为：B')
# elif score>=70:
#     print('您的考试成绩为：C')
# elif score>=60:
#     print('您的考试成绩为：D')
# else:
#     print('您的考试成绩为：E')

# 登录小案例
# users = {'name':'amy','pwd':'123456a'}
# login_name = input('请输入账号名称：')
# login_password = input('请输入账号密码：')
# # if login_name == users.get('name') and login_password==users.get('pwd'):
# if login_name == users['name'] and login_password==users['pwd']:
#     print('您输入的账号密码正确，登录成功')
# else:
#     print('您输入的账号或密码错误，请重新输入')

# python中布尔值：非0为True
# 布尔值为false：None,0,len() ==0
# 条件判断：根据判断语句结果的布尔值执行代码
# if 0:
#     print('哈哈')


# while循环
# 注意：使用while循环时，一定要加上终止循环的条件
# num = 1
# while num<=100:
#     print('第{}遍hello python'.format(num))
#     num+=1

# break 终止当前循环，跳出循环体
# users = {'name':'amy','pwd':'123456a'}
# while True:
#     login_name = input('请输入账号名称：')
#     login_password = input('请输入账号密码：')
#     # if login_name == users.get('name') and login_password==users.get('pwd'):
#     if login_name == users['name'] and login_password==users['pwd']:
#         print('您输入的账号密码正确，登录成功')
#         break
#     else:
#         print('您输入的账号或密码错误，请重新输入')

# continue 终止当前本轮循环，进入下一轮循环
# num = 0
# while num <= 7:
#     num += 1
#     if num ==5:
#         continue
#     print(num)

# for循环
# 内置函数 range（X）返回一个可迭代的对象，可迭代对象有0,1...X-1
# 可迭代对象：能够被for循环遍历的变量，遍历字符串、列表、字典、元组等
# list1 = [11,22,33,44]
# for i in list1:
#     print(i)

# for i in range(1,10,2):
#     print(i)

# str1 = 'cesasas'
# for i in str1:
#     print(i)

# dict1 = {'name':'amy','age':18}
# for i in dict1.values():
#     print(i)
#
# dict1 = {'name':'amy','age':18}
# for i in dict1:
#     print(i)
#
# dict1 = {'name':'amy','age':18}
# for i in dict1.items():
#     print(i)

# foe循环中的break 终止循环
# for i in range(10):
#     if i ==5:
#         break
#     print(i)
# else:
#      print('结束')

# for循环中的continue 中止当前本轮循环，重新开启下一轮循环
# for i in range(10):
#     if i ==5:
#         continue
#     print(i)
# else:
     # 在for循环正常结束时会执行，在break结束循环时不会执行
     # print('结束')

# 循环嵌套
# for i in range(1,10):
#     for j in range (1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print('')

# 函数
# print(type('ces'))
# id()
# 自己定义函数 def
# 作用：用来封装功能，提高代码的复用性
# def add():
#     a = 100
#     b =200
#     print(a+b)
# add()

# 函数返回值 return 只能用于函数内部
# 一个函数只要执行到return,函数就运行结束
# def add():
#     a = 100
#     b = 200
#     return a+b,a-b
# res = add()
# c,d = add()
# print(res)
# print(c,d)
# print('hiahsiuha')

# 函数参数 定义在函数名后面的括号中
#
# def add (a,b):
#     '''
#     实现相加的函数
#     :param a:  int
#     :param b:  int
#     :return:   a+b
#     '''
    # print(a)
    # return a+b
# res1 = add(100,300)     #位置参数
# res2 = add(b=100,a=100) #关键字参数
# print(res1)
# print(res2)
# print(add(100,900))


# 函数不定长参数 *用来打包
# *args 用来接收未被接收的位置参数，保存为一个元组
# **kwargs 用来接收未被接收的关键字参数，保存为一个字典
# def add(a,b,*args,**kwargs):
#     return a,b,args,kwargs
# res1 = add(1,2,3,4,name='amy',age='18')
# print(res1)

# def add1(a,b,*args):
#     print(a)
#     print(b)
#     print(args)
# def add2(a, b, **kwargs):
#     print(a)
#     print(b)
#     print(kwargs)
# res1 = add1('aa','bb','cc','dd')
# res2 = add2('a','b',name = 'Amy',age=18)

# *拆包字符串、列表、元组,只能在函数内使用
# def add(*args):
#     print(args)
# str1 = 'ABCD'
# add(*str1)

# **元组拆包，只能在函数内使用
# def add(**kwargs):
#     print(kwargs)
# dict1 = {'name':'amy','age':18}
# add(**dict1)

# 类方法
# class Hero:
#     # 公共属性
#     attr1 = 100
#     attr2 = 200
#     # 私有属性
#     _attr3 = 300
#     __attr4 = 400
#     def func(self):
#         print('这个是实例方法')
#     # 类方法
#     @classmethod
#     def cls_func(cls,name):
#         print(cls.attr1)
#         cls.name = name
# #     静态方法：不会使用到类属性和实例属性，放单纯的逻辑代码
#     @classmethod
#     def sta_func(cls):
#         print('这个是静态方法')
# Hero.cls_func(name='amy')
# print(Hero.name)

# object为所有类的父类
# 继承：通过继承获取父类所有的属性和方法
# class Phone_v1(object):
#     attr1 = '打电话'
#     def call_phone(self):
#         print('这个是打电话的功能')
# v1 = Phone_v1()
# class Phone_v2(Phone_v1):
#     def send_msg(self):
#         print('这个是发短信的功能')
#     def play_music(self):
#         print('播放音乐')
# v2 = Phone_v2()
# class Phone_v3(Phone_v2):
#     def play_video(self):
#         print('播放视频')
# v3 = Phone_v3()
# class Android(Phone_v3):
#     def android_phone(self):
#         pass
# class Ios(Phone_v3):
#     def ios_phone(self):
#         pass
# v2.call_phone()

# 函数的作用域
# 全局变量:直接定义在模块（py中的变量），在整个文件的任何地方都能访问
# 局部变量:定义在函数中，作用范围仅在当前函数中
# a =100
# def func():
#     b = 110
#     print(b)
#     print(a)

# global
# a = 100
# b = 300
# def func1():
#     global a
#     a = 200   #不能在函数内部重新赋值，如a = a+100
#     print(a)
# func1()
# print(a)
# print(b)

# num = 1000
# def func1():
#     print('func1:',num)
#     def func3():
#         global num  #申明修改全局变量
#         num+=1
#         print('func3:',num)
#     func3()
#     print('func2:',num)
# func1()
# print(num)

"""常见内置函数"""
# list1 = [11,22,33]
# max_value = max(list1)
# print(max_value)
# print(sum(list1))
# print(min(list1))

# enumerate函数 返回一个可枚举的对象，组成一个索引序列
# list1 = [11,22,33,44]
# for i in enumerate(list1):
#     print(i)
# for j in enumerate('abcdefg'):
#     print(j)

# eval函数:识别字符串中的python表达式
# str1 = '[1,2,3,4]'
# print(type(eval(str1)))

# str2 = "print('hello python')"
# print(eval(str2))

# num = eval(input('请输入：'))
# print(type(num))

# filter 过滤
# list1 = [11,22,33,44]
# def func(x):
#     return x >30
# res1 = filter(func,list1)
# print(list(res1))

# map
# list2 = [11,22,33,44,8,67,23]
# res2 = map(func,list2)
# print(list(res2))

# zip() 对序列数据进行聚合打包
# title = ['name','age','gender']
# value = ['Amy',18,'女']
# res1 = zip(title,value)
# print(dict(res1))

# isinstance() 判断数据类型
# str1 = 'aad'
# print(isinstance(str1,str))

# 导入
import test01
game(3)








