"""
===============
author:Administrator
time:14:52
E-mail:1223607348@qq.com
===============
"""
'''
1、用户输入一个数值，请判断用户输入的是否为偶数？是偶数输出True,不是输出False（提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法转换为数值类型，再做判段，）
2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，然后随机生成购买的斤数（5到10斤之间），最后计算出应该支付的金额！
3、现在有列表 li = [‘hello’,‘python18’,‘!’],通过相关操作转换成字符串：'hello python18 !'（注意点:转换之后单词之间有空格）
4、现在有字符串：str1 = 'python hello aaa 123123aabb'
    1、请计算 字符串中有多少个'a'      
    2、请找出字符串中'123'的下标起始位置
    3、请分别判断  'o a'      'he'    'ab'  是否是该字符串中的成员？
'''
# # 1.
# a = int(input('请输入数字:'))
# if a % 2==0:
#     print(True)
# else:
#     print('False')

# # 2.
# import random
# price = float(input('请输入价格:'))
# num = random.randint(5,10)
# totalprice = price*num
# print(totalprice)

# # 3.
# li = ['hello','python18','!']
# res = ' '.join(li)
# print(res)

# 4.
str1 = 'python hello aaa 123123aabb'
print(str1.count('a'))
print(str1.find('123'))
