"""
===============
author:Administrator
time:17:05
E-mail:1223607348@qq.com
===============
"""
import os
from configparser import ConfigParser
from interface_object02.common.constant import CONF_DIR
class MyConfig(ConfigParser):
    '''读取配置文件的类'''
    def __init__(self):
        super().__init__()
        # 初始化时打开配置文件
        conf = os.path.join(CONF_DIR,'conf.ini')
        self.read(conf)
myconf = MyConfig()
# def myconfig():
#     conf = ConfigParser()
#     conf.read(r'E:\Testsoft\python.project\one\python15_object\conf\conf.ini')
#     return conf
# myconf = myconfig()

