"""
===============
author:Administrator
time:11:31
E-mail:1223607348@qq.com
===============
"""
'''
类属性：
    直接定义在类中的变量
    公有属性：
    私有属性：属性名以单下划线或双下划线开头（_attr，__attr2）
类方法：
    通过@classmethod装饰器装饰的方法
    类方法的第一个参数：cls
    cls指的是类本身
    
    
    
静态方法：通过@staticmethod装饰器的方法
'''
# 实例方法：通过实例对象调用
class Hero:
    attr1 = 'hp'
    def func(self):
        pass
    # 类方法：通过类调用
    @classmethod
    def cls_func(cls,attr2):
        print(cls.attr1)
        cls.attr2 = attr2
    # 静态方法：静态方法中不是使用到类属性和实例属性，单纯的逻辑代码
    @staticmethod
    def sta_func():
        print('静态方法')
Hero.cls_func(attr2=11111)
print(Hero.attr2)
Hero.sta_func()