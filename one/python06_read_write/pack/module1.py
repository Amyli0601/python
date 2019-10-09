"""
===============
author:Administrator
time:12:04
E-mail:1223607348@qq.com
===============
"""
# def game(n):
#     win_count = 0
#     total_count = 0
#     draw_count = 0
#     def is_last(i, n, total_count, win_count, draw_count):
#         if i == (n - 1):
#             print('游戏结束，本次游戏场数{}，胜利场数{}，胜率为{}%'.format(
#                 total_count, win_count,
#                 round(100 * win_count / (total_count ), 2)))
#     print('---石头剪刀布游戏开始---\n请按下面提示出拳\n石头【1】 剪刀【2】 布【3】 结束游戏【0】')
#     list1 = ['石头', '剪刀', '布']
#     for i in range(n):
#         total_count += 1
#         user = int(input('请输入您的选项：'))
#         if user == 0:
#             print('结束游戏')
#         else:
#             import random
#             computer = random.randint(1, 3)
#             print('电脑出拳为：', list1[computer - 1])
#             if user == computer:
#                 print('您的出拳为:{},电脑出拳为{},平局'.format(list1[user - 1],
#                                                    list1[computer - 1]))
#                 draw_count += 1
#                 is_last(i, n, total_count, win_count, draw_count)
#                 continue
#             elif user - computer == -1 or user - computer == 2:
#                 print('您的出拳为:{},电脑出拳为{},您胜利了'.format(list1[user - 1],
#                                                      list1[computer - 1]))
#                 win_count += 1
#                 is_last(i, n, total_count, win_count, draw_count)
#                 continue
#             else:
#                 print('您的出拳为:{},电脑出拳为{},您输了'.format(list1[user - 1],
#                                                     list1[computer - 1]))
#
#                 is_last(i, n, total_count, win_count, draw_count)
#                 continue
# # game(3)
def game(n):
    win_count = 0
    total_count = 0
    draw_count = 0
    print('---石头剪刀布游戏开始---\n请按下面提示出拳\n石头【1】 剪刀【2】 布【3】 结束游戏【0】')
    list1 = ['石头', '剪刀', '布']
    while total_count<n:
        total_count += 1
        user = int(input('请输入您的选项：'))
        if user == 0:
            print('结束游戏')
        else:
            import random
            computer = random.randint(1, 3)
            print('电脑出拳为：', list1[computer - 1])
            if user == computer:
                print('您的出拳为:{},电脑出拳为{},平局'.format(list1[user - 1],
                                                   list1[computer - 1]))
                draw_count += 1

                continue
            elif user - computer == -1 or user - computer == 2:
                print('您的出拳为:{},电脑出拳为{},您胜利了'.format(list1[user - 1],
                                                     list1[computer - 1]))
                win_count += 1

                continue
            else:
                print('您的出拳为:{},电脑出拳为{},您输了'.format(list1[user - 1],
                                                     list1[computer - 1]))
    print('游戏结束，本次游戏场数{}，胜利场数{}，胜率为{}%'.format(
                total_count, win_count,
                round(100 * win_count / (total_count ), 2)))
# game(3)
