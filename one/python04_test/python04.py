"""
===============
author:Administrator
time:9:11
E-mail:1223607348@qq.com
===============
"""
#
# 1、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# 如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或
# 20%）和最终价格。
# price = float(input('请输入购买价格：'))
# total_price1 = price*(1-0.1)
# total_price2 = price*(1-0.2)
# if price>=50 and price<=100:
#     print('您的折扣为:10%,您的最终价格为:{:.2f}'.format(total_price1))
# elif price>100:
#     print('您的折扣为:20%,您的最终价格为:{:.2f}'.format(total_price2))
# else:
#     print('您的最终价格为:{:.2f}'.format(price))

# 2、一个 5 位数，判断它是不是回文数。
# 例如： 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。
# i = input('请输入5位数字：')
# if i[0]==i[4] and i[1]==i[3] :
#     print('该数字是回文数')
# else:
#     print('该数字不是回文数')
# 3、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，来猜，
# 如果大于，则打印大于随机数。小了，则打印小于随机数。如果相等，则打印等于随机数
# a = int(input('请输入一个数字：'))
# import random
# b = random.randint(1,9)
# print(b)
# if a>b:
#     print('大于随机数')
# elif a<b:
#     print('小于随机数')
# else:
#     print('等于随机数')
# 4、使用循环和条件语句完成剪刀石头布游戏，提示用户输入要出的拳 ：
# 石头（1）／剪刀（2）／布（3）/退出（4）
# 电脑随机出拳比较胜负，显示用户胜、负还是平局。
# print('请按下面提示出拳\n石头【1】 剪刀【2】 布【3】 退出【4】')
# a = int(input('请输入您的选项：'))
# import random
# b = random.randint(1,3)
# print('电脑出拳:',b)
# while a <4:
#     if a==b:
#         print('平局')
#     elif a==1 and b==2:
#         print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format('石头','剪刀'))
#     elif a==1 and b==3:
#         print('您的出拳为:{}，电脑出拳为:{}，您输了'.format('石头', '布'))
#     elif a==2 and b==1:
#         print('您的出拳为:{}，电脑出拳为:{}，您输了'.format('剪刀', '石头'))
#     elif a==2 and b==3:
#         print('您的出拳为:{}，电脑出拳为:{}，您胜利了'.format('剪刀', '布'))
#     elif a==3 and b==1:
#         print('您的出拳为:{}，电脑出拳为:{}，您胜利了'.format('布', '石头'))
#     elif a==3 and b==2:
#         print('您的出拳为：{}，电脑出拳为：{}，您输了'.format('布', '剪刀'))
#     break
# else:
#     print('游戏结束')