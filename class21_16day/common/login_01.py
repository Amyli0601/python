"""
============================
Author:柠檬班-木森
Time:2019/8/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
日志模块
"""
import logging

"""
调试的方式1：print大法：
调试的方式2:断点调试法
调试的方式3：通过日志来进行调试

logging模块中内置了名叫一个root的日志收集器，收集日志的等级是warning以上的。


"""


logging.debug('---这个是debug等级的日志,一般用于调试')
logging.info('---这个是info等级的日志，常规信息的输出')
logging.warning('---这个是warning等级的日志，警告信息')
logging.error('---这个是error等级的日志，错误信息')
logging.critical('---这个是critical等级的日志，严重的错误，程序要崩溃')













#  日志debug调试方法

# def func(name):
#     print(name,type(name))
#     logging.debug(name)
#     # dict(name)
#
#
# print('-------1-----')
# func('999')


# print('-------2-----')