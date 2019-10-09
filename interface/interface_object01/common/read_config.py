"""
===============
author:Administrator
time:17:05
E-mail:1223607348@qq.com
===============
"""
from configparser import ConfigParser
class MyConfig(ConfigParser):
    '''读取配置文件的类'''
    def __init__(self):
        super().__init__()
        # 初始化时打开配置文件
        self.read(r'E:\Testsoft\python.project\interface\interface_object01\conf\conf.ini')
myconf = MyConfig()
# def myconfig():
#     conf = ConfigParser()
#     conf.read(r'E:\Testsoft\python.project\one\python15_object\conf\conf.ini')
#     return conf
# myconf = myconfig()

