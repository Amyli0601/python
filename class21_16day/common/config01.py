"""
============================
Author:柠檬班-木森
Time:2019/8/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
配置文件：


"""

from configparser import ConfigParser

# 创建一个conf对象
conf = ConfigParser()

# 使用conf对象去打开一个配置文件
conf.read('config.ini', encoding='utf8')

# 通过配置解析器去读取配置文件中的内容
# get方法读取出来的配置项是字符串格式的
age = conf.get('musen', 'age')
print(age, type(age))

# 读取int类型的数据
age = conf.getint('musen', 'age')
print(age, type(age))

# 读取浮点数类型的数据
price = conf.getfloat('musen', 'price')
print(price, type(price))

# 读取布尔类型的数据
swich = conf.getboolean('musen', 'swich')
print(swich, type(swich))

# 查找的方法
# 获取所有的配置项
s = conf.sections()
print(s)

# 获取某一个配置项下面所有的配置内容
o = conf.options('mysql')
print(o)
i = conf.items('mysql')
print(i)

# 查找配置项是否存在（section）
has_s = conf.has_section('mysql')
print(has_s)

# 查找配置项中的某个配置内容是否存在(option)
has_o = conf.has_option('mysql', 'host')
print(has_o)


# 写入内容

# 添加一个配置项[]
# conf.add_section('python11')

# 往某一个配置项中添加数据内容
conf.set('python11','v','3.7')
conf.set('python11','classes','21')

with open('config.ini','w',encoding='utf8') as fp:
    conf.write(fp)
