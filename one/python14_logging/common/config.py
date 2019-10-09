"""
===============
author:Administrator
time:10:25
E-mail:1223607348@qq.com
===============
"""
from configparser import ConfigParser

# 创建一个conf对象
conf = ConfigParser()

# 使用conf对象打开配置文件,指定用utf8格式打开
# conf.read('common.ini',encoding='utf8')

# # 通过配置解析器读取配置文件中的内容
# # get方法读取出来的格式全部为str
# host = conf.get('mysql','host')
# print(host,type(host))
#
# # getint方法：读取int类型数据
# # getfloat方法：读取float类型数据
# # getboolean方法:读取boolean类型数据
# port = conf.getint('mysql','port')
# print(port,type(port))
#
# '''查找的方法'''
# # 查找所有配置项
# all_sec = conf.sections()
# print(all_sec)
# # 获取某一个配置项下面所有的内容
# all_in = conf.options('mysql')
# print(all_in)
# all_items = conf.items('mysql')
# print(all_items)
# # 查找配置项是否存在
# is_exist = conf.has_section('aaa')
# print(is_exist)
# # 查找配置项中的内容是否存在
# has_option = conf.has_option('mysql','host')
# print(has_option)

#
# # 写入内容
# # 添加配置项[]
# conf.add_section('python')
#
# # 往配置项中添加内容
# conf.set('python','vision','1.0.0')
# conf.set('python','class','21')
#
# with open('common.ini','w',encoding='utf8') as fp:
#     conf.write(fp)