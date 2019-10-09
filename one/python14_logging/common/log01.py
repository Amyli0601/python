"""
===============
author:Administrator
time:11:39
E-mail:1223607348@qq.com
===============
"""
'''
调试方法：
1、print输出
2、断点
3、日志输出

logging模块内置了一个root的日志收集器，收集日志的等级是warning以上

'''
import logging

logging.debug('debug等级日志，一般用于调试')
logging.info('info等级日志，常规信息的输出')
logging.warning('waining等级日志，程序出现警告信息')
logging.error('error等级日志，错误信息')
logging.critical('critical等级日志，严重错误信息')











# def fun(name):
#     print(name)
#     dict(name)
# fun('999')