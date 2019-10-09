# -*- coding:utf-8 -*-

import pygame
import sys
import time

from pygame.locals import *

"""
    pygame中，游戏中所有游戏对象，统称为精灵
    游戏引擎

    添加游戏精灵的父类

    编码的步骤：
    1、实现一个基类
    1）继承精灵
    2）定义好三个属性（屏幕、图片、rect）
    3）定义显示方法（在屏幕的指定位置显示图片）

    2、测试基类对象的代码
    1）TankGame类的__init__方法中创建BaseItem的对象（属性）
    2）初始化baseItem对象的image和rect属性
    3）在startGame中的while循环里面，调用baseItem对象的显示方法
"""


class BaseItem(pygame.sprite.Sprite):
    def __init__(self, _screen):
        pygame.sprite.Sprite.__init__(self)  # 初始化精灵里面的属性
        self.image = None;  # 当前游戏精灵的图片
        self.rect = None;  # 位置和大小，x y h w
        self.screen = _screen;  # 游戏屏幕
        self.live = True;  # 精灵是否有效

    def display(self):
        if self.live:
            # 在屏幕中画图片
            self.screen.blit(self.image, self.rect)


class Wall(BaseItem):
    #  定义一个墙类
    IMAGES = []
    IMAGES.append(pygame.image.load('images/walls.gif'))
    IMAGES.append(pygame.image.load('images/water.gif'))
    IMAGES.append(pygame.image.load('images/steels.gif'))
    IMAGES.append(pygame.image.load('images/grass.png'))
    IMAGES.append(pygame.image.load('images/jd.gif'))
    IMAGES.append(pygame.image.load('images/wall.gif'))
    IMAGES.append(pygame.image.load('images/beijin.jpg'))

    def __init__(self, screen, left, top, type_num):
        # 设置初始化属性
        super().__init__(screen)
        self.screen = screen
        self.type = type_num
        self.image = self.IMAGES[self.type]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True
        self.num = 0

    def hit(self):
        if self.type == 0 or self.type == 5:
            # 如果打中的是墙体，让子弹消失，墙也消失，并且发生爆炸
            wm = pygame.sprite.spritecollide(self, TankGame.MISSILE_LIST, True)
            wm += pygame.sprite.spritecollide(self, TankGame.ENMEY_MISSILE_LIST, True)

            if wm and len(wm) > 0:
                for m in wm:
                    # 打中墙体，让子弹消失
                    m.live = False
                    self.num += 1
                    if self.num == 4:
                        # 发生爆炸
                        TankGame.EXPOLE_LIST.append(Expole(self.screen, m.rect.left, m.rect.top))
                        # 墙也消失
                        self.live = False
                        TankGame.WALL_LIST.remove(self)

        elif self.type == 1:
            # 如果 打中的是水，子弹消失，墙没有任何变化

            wm = pygame.sprite.spritecollide(self, TankGame.MISSILE_LIST, True)
            wm += pygame.sprite.spritecollide(self, TankGame.ENMEY_MISSILE_LIST, True)

            if wm and len(wm) > 0:
                # 打中墙体，让子弹消失
                for m in wm:
                    m.live = False
        elif self.type == 2:
            # 打中铁墙，让子弹消失，发生爆炸
            wm = pygame.sprite.spritecollide(self, TankGame.MISSILE_LIST, True)
            wm += pygame.sprite.spritecollide(self, TankGame.ENMEY_MISSILE_LIST, True)

            if wm and len(wm) > 0:
                for m in wm:
                    # 子弹消失
                    m.live = False
                    self.num += 1
                    # 产生爆炸
                    TankGame.EXPOLE_LIST.append(Expole(self.screen, m.rect.left, m.rect.top))
                    if self.num == 100:
                        # 墙也消失
                        self.live = False
                        TankGame.WALL_LIST.remove(self)

        elif self.type == 3:
            # 如果是花则不做任何处理
            pass


class Expole(BaseItem):
    # 定义爆炸类
    IMAGES = []  # 存储所有爆炸显示过程的图片
    for i in range(10):  # 把所有的图片添加进去
        IMAGES.append(pygame.image.load('images/{}.gif'.format(i)))

    def __init__(self, screen, left, top):
        super().__init__(screen)
        # 初始化爆炸对象属性
        self.screen = screen  # 爆炸显示的一个画布
        self.left = left  # 显示的X轴位置
        self.top = top  # 显示Y轴的位置
        self.live = True  # 记录爆炸对象是否有效
        self.num = 0  # 记录爆炸显示的图片

    def display(self):
        # 显示爆炸的方法
        if self.live:
            self.image = Expole.IMAGES[self.num]  # 确定当前显示的爆炸图片
            self.rect = self.image.get_rect()  # 设定图片显示的位置
            self.rect.left = self.left
            self.rect.top = self.top
            self.screen.blit(self.image, self.rect)  # 通过图片和位置，画出爆炸效果
            if self.num < 9:
                self.num += 1
            else:
                self.live = False  # 当显示到最后一张图片的时候，把爆炸对象设为无效状态
                # self.num = 0
        else:
            pass


"""
    坦克类
    1 完善了BaseItem类
    1）在BaseItem类的__init__方法中，添加初始pygame中精灵对象的代码
    2）给每个BaseItem对象，添加了一个live属性（是否是活的属性）
    3）在display中，画图片之前，判断是否是活的（live是否是True）

    2 添加坦克类
    1）添加TANK_IMAGES类属性（定了坦克每个方向的图片）
    2）在__init__方法中，添加坦克的方向属性（缺省值U）
    3）初始了坦克的image和rect属性
    4）在__init__方法的第一行，添加初始父类属性的代码(super().__init__(..))

    3 在TankGame中，将以前的BaseItem对象，改成成Tank对象
    1）TankGame的__init__方法中，创建Tank对象
    2）TankGame的startGame中，调用tank对象的display显示
"""


class Tank(BaseItem):
    TANK_IMAGES = {}  # 存放各个方向的坦克图片，dict类型
    TANK_IMAGES['U'] = pygame.image.load('images/tankU.gif')
    TANK_IMAGES['D'] = pygame.image.load('images/tankD.gif')
    TANK_IMAGES['L'] = pygame.image.load('images/tankL.gif')
    TANK_IMAGES['R'] = pygame.image.load('images/tankR.gif')

    def __init__(self, _screen):
        super().__init__(_screen)
        self.direction = 'U'
        self.image = Tank.TANK_IMAGES[self.direction]
        # 坦克的大小（高  宽）
        self.rect = self.image.get_rect()
        self.rect.left = TankGame.WIDTH / 2
        self.rect.top = TankGame.HEIGHT / 2
        self.screen = _screen

    def hit_wall(self):
        # 判断坦克是否碰撞到墙体  ,如果碰撞到就返回响应的墙体对象
        tw = pygame.sprite.spritecollideany(self, TankGame.WALL_LIST)
        if tw :
            return tw
        else:
            return False



import random


class EnemyTank(Tank):
    # 定义一个敌方坦克类

    def __init__(self, screen):
        # 初始化tank的属性
        super().__init__(screen)
        self.speed = 5  # 定义敌方坦克的速度
        self.direction = random.choice(['U', 'D', 'L', 'R'])  # 随机生成方向
        self.image = Tank.TANK_IMAGES[self.direction]  # 通过方向获取到坦克的图片
        self.rect = self.image.get_rect()
        self.rect.top = random.randint(0, TankGame.HEIGHT - 120)  # 随机生成Y轴的坐标
        self.rect.left = random.randint(0, TankGame.WIDTH - self.rect.width)  # 随机生成x轴的坐标
        self.num = random.randint(20, 40)

    def move(self):
        #  敌方坦克移动的方法
        if self.direction == 'U':  # 当坦克方向朝上的时候
            if self.rect.top <= 0 or self.num == 0:  # 判断坦克是否走到顶，到顶就随机改变方向
                self.direction = random.choice(['U', 'D', 'L', 'R'])
                self.image = Tank.TANK_IMAGES[self.direction]
                self.num = random.randint(20, 40)
            else:
                self.rect.top -= self.speed  # 坦克顶部往上移
                wall = self.hit_wall()
                if wall:
                    num = wall.rect.bottom - self.rect.top
                    self.rect.top += num
                self.num -= 1

        elif self.direction == 'D':  # 当坦克方向朝下的时候
            if self.rect.bottom >= TankGame.HEIGHT or self.num == 0:  # 判断坦克是否走到底部，到底就随机改方向
                self.direction = random.choice(['U', 'D', 'L', 'R'])
                self.image = Tank.TANK_IMAGES[self.direction]
                self.num = random.randint(20, 40)
            else:
                self.rect.bottom += self.speed  # 坦克底部往下移
                wall = self.hit_wall()
                if wall:
                    num = self.rect.bottom - wall.rect.top
                    self.rect.top -= num
                self.num -= 1

        elif self.direction == 'L':  # 当坦克方向往左的时候
            if self.rect.left <= 0 or self.num == 0:  # 判断是否走到最左边，到最左边就换方向
                self.direction = random.choice(['U', 'D', 'L', 'R'])
                self.image = Tank.TANK_IMAGES[self.direction]
                self.num = random.randint(20, 40)
            else:
                self.rect.left -= self.speed  # 坦克的往左边移动
                wall = self.hit_wall()
                if wall:
                    num = wall.rect.right - self.rect.left
                    self.rect.left += num
                self.num -= 1

        elif self.direction == 'R':  # 当坦克方向往右的时候
            if self.rect.right >= TankGame.WIDTH or self.num == 0:  # 判断是否走到最右边，到最右边就换方向
                self.direction = random.choice(['U', 'D', 'L', 'R'])
                self.image = Tank.TANK_IMAGES[self.direction]
                self.num = random.randint(20, 40)
            else:
                self.rect.right += self.speed  # 坦克往右边移动
                wall = self.hit_wall()
                if wall:
                    num = self.rect.right - wall.rect.left
                    self.rect.right -= num
                self.num -= 1

    def random_fire(self):
        if random.randint(1, 101) % 10 == 0:
            TankGame.ENMEY_MISSILE_LIST.add(Missile(self, self.screen))


"""
    主坦克类
    1 添加主坦克类
    1）改变方向的setDirection函数

    2 添加了事件处理代码
    1）dealEvents函数添加了键盘方向键的控制

    3 TankGame类的__init__函数里面，创建MyTank类对象
"""


class MyTank(Tank):
    SPEED = 10  # 主坦克的速度
    IMAGES = {}  # 存放各个方向的坦克图片，dict类型
    IMAGES['U'] = pygame.image.load('images/zhujiU.gif')
    IMAGES['D'] = pygame.image.load('images/zhujiD.gif')
    IMAGES['L'] = pygame.image.load('images/zhujiL.gif')
    IMAGES['R'] = pygame.image.load('images/zhujiR.gif')

    def __init__(self, _screen):
        super().__init__(_screen)

        self.image = self.IMAGES['U']
        self.stop = True  # 是否是停止状态属性
        self.rect.left = 350
        self.rect.top = 650

    def setDirection(self, direct):
        self.direction = direct
        self.image = self.IMAGES[self.direction]

    '''
    移动坦克（根据方向、移动状态，改变坐标信息）
    '''

    def move(self):
        if not self.stop:
            if self.direction == 'U':
                # 往上移动
                self.rect.top = self.rect.top - MyTank.SPEED
                wall = self.hit_wall()
                if wall:
                    num = wall.rect.bottom - self.rect.top
                    self.rect.top += num

                if self.rect.top <= 0:
                    self.rect.top = 0

            elif self.direction == 'D':
                self.rect.bottom = self.rect.bottom + MyTank.SPEED
                wall = self.hit_wall()
                if wall:
                    num = self.rect.bottom - wall.rect.top
                    self.rect.top -= num

                if self.rect.bottom >= TankGame.HEIGHT:
                    self.rect.bottom = TankGame.HEIGHT

            elif self.direction == 'L':
                self.rect.left = self.rect.left - MyTank.SPEED
                wall = self.hit_wall()
                if wall:
                    num = wall.rect.right - self.rect.left
                    self.rect.left += num
                if self.rect.left <= 0:
                    self.rect.left = 0

            elif self.direction == 'R':
                self.rect.right = self.rect.right + MyTank.SPEED
                wall = self.hit_wall()
                if wall:
                    num = self.rect.right - wall.rect.left
                    self.rect.right -= num
                if self.rect.right >= TankGame.WIDTH:
                    self.rect.right = TankGame.WIDTH

    def fire(self):
        #  发射子弹的方法
        return Missile(self, self.screen)




"""
   实现退出游戏功能
   1、添加退出游戏的代码（方法）
   2、点击窗口关闭按钮的时候，调用退出游戏的方法，退出游戏
"""


class Missile(BaseItem):
    SPEED = 12  # 子弹的速度
    WIDTH = 12  # 子弹的宽度
    HEIGTH = 12  # 子弹的高度
    IMAGES_LIST = {}  # 储存 子弹的图片
    IMAGES_LIST['U'] = pygame.image.load('images/missileD.gif')
    IMAGES_LIST['D'] = pygame.image.load('images/missileU.gif')
    IMAGES_LIST['L'] = pygame.image.load('images/missileL.gif')
    IMAGES_LIST['R'] = pygame.image.load('images/missileR.gif')

    def __init__(self, tank, screen):
        BaseItem.__init__(self, screen)
        self.direction = tank.direction  # 根据坦克的方向，确定子弹的方向
        self.image = Missile.IMAGES_LIST[self.direction]  # 根据方向确定子弹所使用的图片
        self.rect = self.image.get_rect()  # 过去子弹边缘位置

        if self.direction == 'U':  # 如果坦克朝上
            self.rect.top = tank.rect.top  # 子弹的Y  在坦克的顶部
            self.rect.left = tank.rect.left + tank.rect.width // 2 - 5  # 坦克左边位置加上坦克宽的的二分之一

        elif self.direction == 'D':  # 如果坦克朝下
            self.rect.top = tank.rect.bottom - 7  # 子弹的Y  在坦克的底部
            self.rect.left = tank.rect.left + tank.rect.width // 2 - 7  # 坦克左边位置加上坦克宽的的二分之一

        if self.direction == 'L':  # 如果坦克朝左
            self.rect.top = tank.rect.top + tank.rect.height // 2 - 3  # 子弹的Y顶部+  在坦克的高度的分之一
            self.rect.left = tank.rect.left  # x轴坦克左边位置

        if self.direction == 'R':  # 如果坦克朝右
            self.rect.top = tank.rect.top + tank.rect.height // 2 - 2  # 子弹的Y顶部+  在坦克的高度的2分之一
            self.rect.left = tank.rect.right - 7  # x轴坦克右边位置

    def move(self):
        #  子弹移动的方法
        if self.direction == 'U':  # 子弹方向往上的时候
            if self.rect.top < 0:
                self.live = False
            else:
                self.rect.top = self.rect.top - Missile.SPEED
        elif self.direction == 'D':  # 子弹往下的时候
            if self.rect.top > TankGame.HEIGHT:
                self.live = False
            else:
                self.rect.top = self.rect.top + Missile.SPEED
        elif self.direction == 'L':  # 子弹往左的时候
            if self.rect.left < 0:
                self.live = False
            else:
                self.rect.left = self.rect.left - Missile.SPEED
        elif self.direction == 'R':  # 子弹往右的时候
            if self.rect.left > TankGame.WIDTH:
                self.live = False
            else:
                self.rect.left = self.rect.left + Missile.SPEED

    def hit(self):
        # 判断子弹是否集中坦克
        # 1.判断主坦克子弹是否打中敌方坦克
        for e_tank in TankGame.ENMEY_TANK_LIST:
            # 1.1遍历出所有的敌方坦克
            tm = pygame.sprite.spritecollide(e_tank, TankGame.MISSILE_LIST, True)
            if tm and len(tm) > 0:
                #  1.2主坦克击中敌方坦克
                # 让敌方坦克消失
                e_tank.live = False
                TankGame.ENMEY_TANK_LIST.remove(e_tank)
                # 让子弹消失
                # for m in tm:
                #     m.live = False
                #     TankGame.MISSILE_LIST.remove(m)
                # 创建爆炸对象,实现爆炸效果,
                TankGame.EXPOLE_LIST.append(Expole(self.screen, e_tank.rect.left, e_tank.rect.top))

        # 2、判断敌方子弹是否击中主坦克
        mm = pygame.sprite.spritecollide(TankGame.MYTANK_LIST[0], TankGame.ENMEY_MISSILE_LIST, True)
        if mm and len(mm) > 0:
            # 让子弹消失
            for m in mm:
                m.live = False
                TankGame.ENMEY_MISSILE_LIST.remove(m)
            # 创建爆炸对象，显示爆炸效果
            TankGame.EXPOLE_LIST.append(
                Expole(self.screen, TankGame.MYTANK_LIST[0].rect.left, TankGame.MYTANK_LIST[0].rect.top))


class TankGame(object):
    WIDTH = 900
    HEIGHT = 700
    GAME_NAME = '坦克游戏'

    MISSILE_LIST = pygame.sprite.Group()  # 存储主子弹的列表

    ENMEY_TANK_LIST = []  # 存储敌方坦克

    ENMEY_MISSILE_LIST = pygame.sprite.Group()  # 存储敌方坦克的子弹

    EXPOLE_LIST = []  # 储存所有的爆炸对象

    MYTANK_LIST = []  # 储存主坦克

    WALL_LIST = pygame.sprite.Group()  # 存储墙
    BEIJIN_LIST = []

    def __init__(self):
        # 画一个屏幕，指定宽 高 窗口大小不可不变 不是全屏
        self.screen = pygame.display.set_mode((TankGame.WIDTH, TankGame.HEIGHT), 0, 32)
        # 设置窗口的标题
        pygame.display.set_caption(TankGame.GAME_NAME)

        # 测试基类的对象
        self.tank = MyTank(self.screen)
        TankGame.MYTANK_LIST.append(self.tank)
        for i in range(6):
            for j in range(8):
                TankGame.BEIJIN_LIST.append(Wall(self.screen,j*128,i*128,6))

        # 创建基地
        TankGame.WALL_LIST.add(Wall(self.screen, 435, 650, 4)) #  基地
        #  基地保护墙
        TankGame.WALL_LIST.add(Wall(self.screen, 400, 680, 5))
        TankGame.WALL_LIST.add(Wall(self.screen, 400, 650, 5))
        TankGame.WALL_LIST.add(Wall(self.screen, 400, 620, 5))
        TankGame.WALL_LIST.add(Wall(self.screen, 430, 620, 5))
        TankGame.WALL_LIST.add(Wall(self.screen, 460, 620, 5))
        TankGame.WALL_LIST.add(Wall(self.screen, 490, 620, 5))
        TankGame.WALL_LIST.add(Wall(self.screen, 490, 650, 5))
        TankGame.WALL_LIST.add(Wall(self.screen, 490, 680, 5))

        #  创建墙
        # set1 = {(0,1),}
        # for a in range(10):
        #     for a in range(15):
        #         j = random.randint(0,15)
        #         i = random.randint(0,8)
        #         set1.add((j,i))
        #
        #
        # for item in set1:
        #     TankGame.WALL_LIST.add(Wall(self.screen, item[0]*60, item[1]*60, random.choice([0,0,0,0,1,2,3])))



        TankGame.WALL_LIST.add(Wall(self.screen, 180, 520, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 180, 580, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 180, 640, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 240, 100, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 300, 100, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 360, 100, 0))
        #
        TankGame.WALL_LIST.add(Wall(self.screen, 120, 0, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 120, 60, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 120, 120, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 120, 180, 3))
        TankGame.WALL_LIST.add(Wall(self.screen, 120, 240, 3))
        TankGame.WALL_LIST.add(Wall(self.screen, 120, 300, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 120, 360, 0))

        TankGame.WALL_LIST.add(Wall(self.screen, 180, 360,0))
        TankGame.WALL_LIST.add(Wall(self.screen, 240, 360, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 300, 360, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 360, 360, 1))
        TankGame.WALL_LIST.add(Wall(self.screen, 420, 360, 1))
        TankGame.WALL_LIST.add(Wall(self.screen, 480, 360, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 300, 120, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 300, 180, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 660, 0, 2))
        TankGame.WALL_LIST.add(Wall(self.screen, 660, 60, 2))
        TankGame.WALL_LIST.add(Wall(self.screen, 660, 120, 3))

        TankGame.WALL_LIST.add(Wall(self.screen, 180, 60,3))
        TankGame.WALL_LIST.add(Wall(self.screen, 240, 60, 3))
        TankGame.WALL_LIST.add(Wall(self.screen, 300, 60, 2))
        TankGame.WALL_LIST.add(Wall(self.screen, 360, 60, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 420, 60, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 480, 60, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 0, 0, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 0, 60, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 0, 120, 1))
        TankGame.WALL_LIST.add(Wall(self.screen, 0, 180, 1))
        TankGame.WALL_LIST.add(Wall(self.screen, 0, 240, 2))
        TankGame.WALL_LIST.add(Wall(self.screen, 0, 300, 2))
        TankGame.WALL_LIST.add(Wall(self.screen, 0, 360, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 60, 480, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 120, 480, 3))
        TankGame.WALL_LIST.add(Wall(self.screen, 180, 480, 3))
        TankGame.WALL_LIST.add(Wall(self.screen, 240, 480, 0))

        TankGame.WALL_LIST.add(Wall(self.screen, 360, 480, 2))
        TankGame.WALL_LIST.add(Wall(self.screen, 420, 480, 2))
        TankGame.WALL_LIST.add(Wall(self.screen, 480, 480, 2))
        TankGame.WALL_LIST.add(Wall(self.screen, 540, 480, 3))
        TankGame.WALL_LIST.add(Wall(self.screen, 600, 480, 1))
        TankGame.WALL_LIST.add(Wall(self.screen, 660, 480, 1))
        TankGame.WALL_LIST.add(Wall(self.screen, 720, 480, 0))

        TankGame.WALL_LIST.add(Wall(self.screen, 780, 480, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 780, 420,0))
        TankGame.WALL_LIST.add(Wall(self.screen, 780, 360, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 780, 300, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 780, 240, 0))

        TankGame.WALL_LIST.add(Wall(self.screen, 780, 180,0))
        TankGame.WALL_LIST.add(Wall(self.screen, 720, 180, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 660, 180, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 600, 180, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 540, 180, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 480, 180, 0))
        TankGame.WALL_LIST.add(Wall(self.screen, 480, 120, 0))

        for i in range(10):  # 游戏开始，生成10个敌方tank
            TankGame.ENMEY_TANK_LIST.append(EnemyTank(self.screen))  # 把生成的tank存储到敌方坦克列表里


    '''
    开始游戏
    '''

    def startGame(self):
        while True:
            # 每循环一次，把以前的屏幕清除
            self.screen.fill((0, 0, 0))
            # 获取窗口的事件
            self.dealEvents()
            # 移动主坦克
            self.tank.move()
            for b in TankGame.BEIJIN_LIST:
                b.display()

            for wall in TankGame.WALL_LIST:
                wall.hit()
                wall.display()

            for expole in TankGame.EXPOLE_LIST:  # 遍历爆炸的列表
                expole.display()  # 显示该爆炸对象

            for m in TankGame.MISSILE_LIST:  # 遍历主坦克子弹列表里面所有的子弹，并且显示出来
                if m.live == True:
                    m.hit()
                    m.move()
                    m.display()
                else:
                    TankGame.MISSILE_LIST.remove(m)

            for e_tank in TankGame.ENMEY_TANK_LIST:  # 显示敌方坦克
                if e_tank.live == True:
                    e_tank.move()
                    e_tank.random_fire()
                    e_tank.display()
                else:
                    TankGame.ENMEY_TANK_LIST.remove(e_tank)

            for em in TankGame.ENMEY_MISSILE_LIST:  # 显示敌方子弹
                if em.live == True:
                    em.hit()
                    em.move()
                    em.display()
                else:
                    TankGame.ENMEY_MISSILE_LIST.remove(em)

            # 让我们的程序休息0.05秒
            time.sleep(0.05)
            # 测试基类，是否真的可以显示要画的图片
            self.tank.display()
            # 显示一次
            pygame.display.update()

    '''
    处理游戏窗口中的事件
    '''

    def dealEvents(self):
        # 处理关闭事件（判断当前的事件是否是关闭事件，如果是，调用exitGame函数）
        # 1 获取当前事件
        eventList = pygame.event.get()
        for e in eventList:
            # 2 判断是什么事件
            # 3 根据不同事件，做对应的处理
            if e.type == QUIT:
                self.exitGame()
            if e.type == KEYDOWN:
                if e.key == K_UP:  # 向上的方向键
                    # 改变方向
                    self.tank.setDirection('U')
                    # 将当前坦克设置成移动状态
                    self.tank.stop = False
                    # 移动
                    # self.tank.move();
                if e.key == K_DOWN:  # 向下的方向键
                    self.tank.setDirection('D')
                    self.tank.stop = False
                    # self.tank.move();
                if e.key == K_LEFT:  # 向左的方向键
                    self.tank.setDirection('L')
                    self.tank.stop = False
                    # self.tank.move();
                if e.key == K_RIGHT:  # 向右的方向键
                    self.tank.setDirection('R')
                    self.tank.stop = False
                    # self.tank.move();

                if e.key == K_SPACE:  # 空格键发射子弹
                    m = self.tank.fire()
                    TankGame.MISSILE_LIST.add(m)  # 把子弹添加到列表里面

            if e.type == KEYUP:
                self.tank.stop = True

    '''
    退出游戏
    '''

    def exitGame(self):
        # 退出python的运行环境
        sys.exit()
        # pass;


if __name__ == '__main__':
    game = TankGame()
    game.startGame()
