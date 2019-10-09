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
    """读取配置文件的类"""
    def __init__(self):
        super().__init__()

        # 初始化的时候，打开配置文件
        self.read(r'C:\project\python21\class21_api_project\conf\conf.ini')

myconf = MyConfig()


