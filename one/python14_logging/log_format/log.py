"""
===============
author:Administrator
time:15:41
E-mail:1223607348@qq.com
===============
"""
import logging
# 第一步：创建日志收集器,设置收集日志的等级
my_log = logging.getLogger('my_log')
my_log.setLevel('DEBUG')
# 第二步：创建日志输出渠道，输出到控制台
sh = logging.StreamHandler()
sh.setLevel('INFO')

fh = logging.FileHandler('log.log','a',encoding='utf8')
fh.setLevel('DEBUG')

# 第三步：将日志输出渠道添加到日志收集器
my_log.addHandler(sh)
my_log.addHandler(fh)

# 第四步:指定日志输出的格式
fot = '%(asctime)s--[%(filename)s--line:%(lineno)s]--日志等级:%(levelname)s--具体内容：%(message)s'
# 创建日志格式对象
formatter = logging.Formatter(fot)
# 将日志格式绑定到输出渠道
sh.setFormatter(formatter)
fh.setFormatter(formatter)

# 第五步:输出日志内容
my_log.debug('debug等级日志，一般用于调试')
my_log.info('info等级日志，常规信息的输出')
my_log.warning('waining等级日志，程序出现警告信息')
my_log.error('error等级日志，错误信息')
my_log.critical('critical等级日志，严重错误信息')