"""
============================
Author:柠檬班-木森
Time:2019/8/27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import logging


class MyLogging(object):

    def __new__(cls, *args, **kwargs):
        # 创建对象的
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
        return my_log



# 创建一个日志收集器对象
log = MyLogging()


