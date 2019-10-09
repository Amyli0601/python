"""
===============
author:Administrator
time:11:42
E-mail:1223607348@qq.com
===============
"""
"""
模块导入
1、import 模块名
2、from 模块名 import 函数名/变量/类

包导入
from 包名 import 模块一名1，模块2
from 包名.模块名 import 函数名/变量名
"""
# from python06 import main2,books
# print(books)
# from python06 import print_menu as pm
# pm()

# from pack import module1
# module1.game(2)

# import sys
# from pack.module1 import game
# game(2)

'''
文件的操作
1、文件打开和关闭
    打开：open()
    关闭：close()
2、文件内容写入
    write:写入数据(写入内容必须为字符串)
    writelines:写入多条数据(内容是可迭代对象列表)
3、文件内容读取
    read()
    readline():读取一行内容
    readlines():按行读取所有内容，每一行作为一个元素，放入列表中
4、文件打开的方式
    r:只读模式打开，文件不存在会报错
    w:写入的模式打开，如果文件不存在，创建一个新文件;
                    文件存在，清空原来的内容重新写入
    a:写入的模式打开，如果文件不存在，创建一个新文件;
                    文件存在，在原来的内容的尾部继续写入

'''
# list1 =['aa','bb','cc']
# def file_write():
    # w = open('test.txt','w',encoding='utf8')
    # w.write('测试')
    # a = open('test.txt','a',encoding='utf8')
    # a.write('python'+'\n')
#     a.write(str(list1))
#     a.writelines(list1)
#     a.close()
# file_write()

# def file_read():
#     r = open('test.txt', 'r')
#     r.close()
# file_read()



# 打开同级目录文件
# r = open ('book.txt','r',encoding='utf8')
# print(r)
# 文件内容读取
# content = r.read()
# print(content)
# print(r.readline())
# print(r.readlines())
# 关闭文件
# r.close()

'''上下文管理器:会自动关闭文件'''
with open('test.txt','r',encoding='utf8') as new:
    print(new.read())
