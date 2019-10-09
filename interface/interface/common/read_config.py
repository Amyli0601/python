"""
===============
author:Administrator
time:17:05
E-mail:1223607348@qq.com
===============
"""
import os
from interface.common.constant import CONF_DIR

from configparser import ConfigParser



switch_file_path = os.path.join(CONF_DIR,'env.ini')
class MyConfig(ConfigParser):
    '''读取配置文件的类'''
    def __init__(self):
        super().__init__()

        c = ConfigParser()
        c.read(switch_file_path,encoding='utf8')
        env = c.getint('env','switch')
        # 根据开关的值，分别去读取不同环境的配置文件
        if env==1:
            self.read(os.path.join(CONF_DIR,'conf.ini'),encoding='utf8')
        elif env==2:
            self.read(os.path.join(CONF_DIR, 'conf_qc.ini'), encoding='utf8')
        else:
            self.read(os.path.join(CONF_DIR, 'conf.ini'), encoding='utf8')
myconf = MyConfig()
# def myconfig():
#     conf = ConfigParser()
#     conf.read(r'E:\Testsoft\python.project\one\python15_object\conf\conf.ini')
#     return conf
# myconf = myconfig()

