"""
============================
Author:柠檬班-木森
Time:2019/8/27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from configparser import ConfigParser


class MyConfig(ConfigParser):

    def __init__(self):
        super().__init__()

        # 初始化的时候，打开配置文件
        self.read(r'C:\project\python21\py21_apt_test\conf\conf.ini')

myconf = MyConfig()

#
# def myconfig():
#     conf = ConfigParser()
#     conf.read(r'C:\project\python21\py21_apt_test\conf\conf.ini')
#     return conf
#
#
# my_conf = myconfig()
