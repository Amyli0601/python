"""
===============
author:Administrator
time:10:43
E-mail:1223607348@qq.com
===============
"""
'''
继承
    object：python中所有类的父类
    作用：
重写父类方法：
    在子类中重新定义和父类相同的方法

'''
# class BsaePhone(object):
#     attr = '移动手机'
#     def call_phone(self):
#         print('打电话')
#     def func(self):
#         print('测试')
# class NewPhone01(BsaePhone):
#     attr = '智能'
#     def send_info(self):
#         print('发短信')
#     def func(self):
#         # 在子类中，调用父类同名的方法
#         # 方法1、父类名.方法名()
#         BsaePhone.func(self)
#         # 方法2、super().方法名(self)
#         super().func()
#         print('ces')
# v2 = NewPhone01()
# # 子类的对象调用和父类同名的方法时，优先调用自身的方法和属性
# v2.func()
# # print(v2.attr)
# # print(BsaePhone.attr)

'''
魔术方法：在python中用双下划线开头双下划线结尾的方法
魔术方法在特定情况下自动调用，不需要手动去调用
__init__:创建对象时自动调用
__setattr__:
__getattr__:
__delattr__:
__new__:
魔术变量:在python中用双下划线开头双下划线结尾的变量
__file__:当前文件的绝对路径
__name__:__main__
__main__:代表当前启用文件

内置函数
setattr
getattr
delattr
'''
class Hero(object):
    attr=1000
    # def __setattr__(self, key, value):
    #     # 该方法在对象设置属性时被自动调用
    #     print('self:{}--key:{}--value:{}'.format(self,key,value))
    #     # 调用父类的__setattr__方法
    #     super().__setattr__(key, value)
# 创建一个对象
# h1 = Hero()
# h1.attr1 = 100
# # 利用反射机制，动态设置属性
# setattr(h1,'name','可乐')
# h1.age = 25
# # 获取属性
# res1 = getattr(h1,'name')
# print(res1)
# # 删除实例对象属性
# print(h1.attr1)
# delattr(h1,'attr1')
# # 删除类属性
# print(Hero.attr)
# delattr(Hero,'attr')
# print(Hero.attr)
# print(h1.name)

# 魔术变量
print(__file__)
print(__name__)
print(Hero)