"""
===============
author:Administrator
time:18:30
E-mail:1223607348@qq.com
===============
"""
'''
面向对象
类：
    语法：class 类名 class 类名(object):
    类名规范：每一个单词的首字母大写
    类中可以描述这一类事务的属性和方法  
属性：
    类属性：每一个实例对象而且值是一样的，定义在类中的变量
    实例属性：通过实例对象.属性名进行赋值,实例属性是该实例对象独有的，其他对象无法调用
属性的访问：
    类属性：可以通过实例对象/类获取
    实例属性：只能通过实例访问
方法:定义在类中的函数
    实例方法：
        self:代表实例对象，通过实例对象时可以不传，通过类调用时需传实例对象
    类方法：
对象：
'''
# class Human():
#     attr1 = '有头发'
#     attr2 = '两只手'
#     attr3 = '五官'
#     def skills(self):
#         print('{}调用了技能1:说话'.format(self.name))
# human1 = Human()
# human2 =Human()
# # 实例属性
# human1.name = 'lucky'
#
# # print(human1.attr1)
# # print(Human.attr2)
# # print(human1.name)
#
# # 通过实例对象调用实例方法
# human1.skills()
# # 通过类调用实例方法
# Human.skills(human1)

class Human:
    attr1 = '手'
    attr2 = '头发'
    def __init__(self,name,age):
        '''初始化方法：在创建对象时自动调用'''
        self.name = name
        self.age = age
man1 = Human('可乐',24)
man2 = Human('lucky',18)
print(man1.name)
print(man2.name)
