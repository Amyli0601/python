def game(n):
    win_count = 0
    total_count = 0
    draw_count = 0
    def is_last(i, n, total_count, win_count, draw_count):
        if i == (n - 1):
            print('游戏结束，本次游戏场数{}，胜利场数{}，胜率为{:%}'.format(
                total_count, win_count, win_count / (total_count - draw_count)))
    print('---石头剪刀布游戏开始---\n请按下面提示出拳\n石头【1】 剪刀【2】 布【3】 退出【4】')
    list1 = ['石头', '剪刀', '布']
    for i in range(n):
        total_count += 1
        user = int(input('请输入您的选项：'))
        import random
        computer = random.randint(1, 3)
        print('电脑出拳为：', list1[computer - 1])
        if user == computer:
            print('您的出拳为:{},电脑出拳为{},平局'.format(list1[user - 1],
                                               list1[computer - 1]))
            draw_count += 1
            # if i == (n - 1):
            #     print('游戏结束，本次游戏场数{}，胜利场数{}，胜率为{}'.format(
            #         total_count, win_count,
            #         win_count / (total_count - draw_count)))
            is_last(i, n, total_count, win_count, draw_count)
            continue
        elif user - computer == -1 or user - computer == 2:
            print('您的出拳为:{},电脑出拳为{},您胜利了'.format(list1[user - 1],
                                                 list1[computer - 1]))
            win_count += 1

            # if i == (n - 1):
            #     print('游戏结束，本次游戏场数{}，胜利场数{}，胜率为{}'.format(
            #         total_count, win_count,
            #         win_count / (total_count - draw_count)))
            is_last(i, n, total_count, win_count, draw_count)
            continue
        else:
            print('您的出拳为:{},电脑出拳为{},您输了'.format(list1[user - 1],
                                                list1[computer - 1]))

            # if (i == n):
            #     print('游戏结束，本次游戏场数{}，胜利场数{}，胜率为{}'.format(
            #         total_count, win_count,
            #         win_count / (total_count - draw_count)))
            is_last(i, n, total_count, win_count, draw_count)
            continue


game(3)