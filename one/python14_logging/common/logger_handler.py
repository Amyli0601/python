"""
===============
author:Administrator
time:15:12
E-mail:1223607348@qq.com
===============
"""
'''
设置日志输出渠道
'''
import logging
# 第一步：创建日志收集器
mylog = logging.getLogger()
mylog.setLevel('DEBUG')

# 第二步：设置输出渠道
# 1、输出到控制台
sh = logging.StreamHandler()
sh.setLevel('INFO')
# 2、输出到文件
fh = logging.FileHandler(filename='my_log',mode='a',encoding='utf8')
fh.setLevel('INFO')

# 第三步：将渠道添加到日志收集器
mylog.addHandler(sh)
mylog.addHandler(fh)

# 第四步：日志输出
mylog.debug('debug等级日志，一般用于调试')
mylog.info('info等级日志，常规信息的输出')
mylog.warning('waining等级日志，程序出现警告信息')
mylog.error('error等级日志，错误信息')
mylog.critical('critical等级日志，严重错误信息')

# 设置日志输出格式
formatter = logging.Formatter('')