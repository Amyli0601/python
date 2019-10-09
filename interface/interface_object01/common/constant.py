"""
===============
author:Administrator
time:16:57
E-mail:1223607348@qq.com
===============
"""
'''
常量模块：
获取项目目录的路径，保存

项目路径：
用例类路径
配置文件的路径：打开配置文件的路径
用例数据的路径
日志文件的路径:输出日志的路径
测试报告的路径
'''
import os
# res = os.path.dirname(os.path.dirname(__file__))
# print(res)
# 自动获取项目目录路径
OBJECT_DIR = os.path.dirname(os.path.dirname(__file__))
# print(OBJECT_DIR)
# 测试用例类路径路径
CASE_DIR = os.path.join(OBJECT_DIR,'testcases')
# print(CASE_DIR)
# 测试报告所在目录路径
TRPORT_DIR = os.path.join(OBJECT_DIR,'reports')
# 日志文件所在目录路径
LOG_DIR = os.path.join(OBJECT_DIR,'logs')
# 用例数据所在目录路径
DATA_DIR = os.path.join(OBJECT_DIR,'datas')
# 配置文件所在目录路径
CONF_DIR = os.path.join(OBJECT_DIR,'conf')