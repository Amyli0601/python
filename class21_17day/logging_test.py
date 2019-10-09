"""
============================
Author:柠檬班-木森
Time:2019/8/27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import logging

# 第一步 创建一个日志收集器
my_log = logging.getLogger('my_log')
my_log.setLevel('DEBUG')

# 第二步：创建日志输出渠道
sh = logging.StreamHandler()
sh.setLevel('INFO')

fh = logging.FileHandler('log.log', encoding='utf8')
fh.setLevel('DEBUG')

# 第三步：将日志收集器和输出渠道进行绑定

my_log.addHandler(sh)
my_log.addHandler(fh)


# 指定日志输出的格式
fot = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
# 创建日志格式对象
formatter = logging.Formatter(fot)
# 输出格式绑定的输出渠道
sh.setFormatter(formatter)
fh.setFormatter(formatter)




my_log.debug('---这个是debug等级的日志,一般用于调试')
my_log.info('---这个是info等级的日志，常规信息的输出')
my_log.warning('---这个是warning等级的日志，警告信息')
my_log.error('---这个是error等级的日志，错误信息')
my_log.critical('---这个是critical等级的日志，严重的错误，程序要崩溃')
