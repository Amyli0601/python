"""
===============
author:Administrator
time:16:39
E-mail:1223607348@qq.com
===============
"""
'''
os模块 和操作系统交互的
相对路径：
.代表当前目录下
..代表上一级目录
绝对路径：电脑硬盘中的文件路径
'''
import os
# 获取当前的工作路径
# 获取后只能打开当前目录下文件或用绝对路径打开其他目录下文件
# print(os.getcwd())
# with open('book.txt','r',encoding='utf8') as new:
#     print(new.read())
# with open(r'E:\Testsoft\python.project\one\python06_read_write\book.txt','r',encoding='utf8') as new1:
#     print(new1.read())

# 切换工作路径
# os.chdir(r'E:\Testsoft\python.project\one\python06_read_write\practice06_file')
# print(os.getcwd())

# 切换到上一级目录
# os.chdir('..')
# print(os.getcwd())

# 添加目录
# os.mkdir('test01.py')

# 删除目录
# os.rmdir('test01.py')

# 获取当前目录下的目录和文件
# print(os.listdir('.'))
# print(os.listdir(r'E:\Testsoft\python.project\one\package_test01'))

# 判断传入路径是否为目录
# res = os.path.isdir(r'E:\Testsoft\python.project\one\package_test01')
# print(res)

# 判断传入路径是否为文件
# res1 = os.path.isfile(r'E:\Testsoft\python.project\one\package_test01')
# print(res1)

#获取当前文件父级的绝对路径
# res2 = os.path.dirname(__file__)
# print(res2)

'''
异常处理
1、异常分析，找到错误点
2、异常处理
关键字
try:必要
    可能出现错误的代码
except:必要
    try里面的代码出现了异常，对错误处理的代码
else:非必要
    try里面的代码没有出现异常，执行的代码
finally:非必要
    不管try里面的代码有没有错误均会执行
'''
# try:
#     with open('test.txt','r',encoding='utf8') as new:
#         print(new.read())
# except:
#     new1 = open('test.txt', 'w', encoding='utf8')
#     print(new1.write('测试'))
#     new1.close()
# else:
#     print('代码没有错误')
# finally:
#     print('finally')

'''
复制指定路径下所有文件到新的文件
'''
# import os
# def copy_file(path):
#     '''
#
#     :param path: 目标路径
#     :return:
#     '''
#     # 切换路径，获取目标目录中所有的文件和目录
#     # os.chdir(path)
#     try:
#         file_list = os.listdir(r'E:\Testsoft\python.project\one\python07_path_error')
#     except:
#         print('路径不正确')
#     else:
#         # 遍历目录路径所有的目录和文件
#         for i in file_list:
#             # 判断是否为文件
#             if os.path.isfile(i):
#                 # 如果是文件，打开文件，读取文件
#                 with open(i,'r',encoding='utf8') as new:
#                     content = new.read()
#                 # 复制文件，写入内容
#                 with open('copy_'+i,'w',encoding='utf8') as new:
#                     new.write(content)
# copy_file(r'E:\Testsoft\python.project\one\python07_path_error')

'''
捕获指定多种异常类型
'''
# 方法一
# dict1 = {'key':'1213a'}
# try:
#     print(dict1['key1'])
# except KeyError as e:
#     print('代码发生错误：{}'.format(e))
# except NameError as e:
#     print('代码发生错误：{}'.format(e))
# else:
#     print('代码正常')

# 方法二

# dict1 = {'key':'1213a'}
# try:
#     print(dict1['key1'])
# except (KeyError,NameError) as e:
#     print('代码发生错误：{}'.format(e))
# else:
#     print('代码正常')

# 方法三：通过基类捕获异常
# dict1 = {'key':'1213a'}
# try:
#     print(dict1['key1'])
# except Exception as e:
#     print('代码发生错误：{}'.format(e))
# else:
#     print('代码正常')

'''
raise:主动抛出异常
'''
dict1 = {'key':'1213a'}
try:
    print(dict1['key1'])
except Exception as e:
    print('代码发生错误：{}'.format(e))
    raise e
else:
    print('代码正常')











