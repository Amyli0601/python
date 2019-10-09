import pygame
import time
import sys

from  pygame.locals import QUIT,KEYDOWN,KEYUP

#第一步：定义游戏类

class TankGame(object):
    TANKLIST = []

    #游戏初始化的方法
    def __init__(self):
        #设置游戏窗口的大小
        self.screen= pygame.display.set_mode((600,500),0,32)
        #设置游戏窗口的标题
        pygame.display.set_caption('坦克大战')
        my_tank = Tank(self.screen)
        TankGame.TANKLIST.append(my_tank)

    #游戏开始的方法
    def start_game(self):
        while True:
            #只显示一次窗口内容
            self.get_elenvt()   #每一次循环，都要检测当前游戏窗口中的事件
            time.sleep(0.5)

            for t in TankGame.TANKLIST:
                t.display()
            pygame.display.update()

    #事件检测的方法
    def get_elenvt(self):
        #获取游戏中的事件
        elevt_list = pygame.event.get()
        #遍历出来所有的事件
        for e in elevt_list:
            #判断事件的类型
            if e.type == QUIT:  #如果时退出事件，就调用退出游戏的方法
                self.exit_game()


    #游戏退出的方法
    def exit_game(self):
        sys.exit()  #退出当前python的运行环境，游戏直接结束




#定义所有游戏精灵的父类（基类）
class BaseGame(pygame.sprite.Sprite):

    def __init__(self,_screen):
        super().__init__()
        #为游戏精灵设置共有初始化属性
        self.image = None
        self.rect = None
        self.live = True  #表示对象是否有效
        self._screen = _screen

    def display(self):
        #判断游戏精灵是否有效，显示游戏精灵
        if self.live ==True:
            self._screen.blit(self.image,self.rect)

#定义坦克类，继承游戏精灵的父类

class Tank(BaseGame):
    #定义字典，用来存放坦克所有形态的图片
    TANK_IMAGE = {}
    TANK_IMAGE['U'] = pygame.image.load('./images/tankU.gif')
    TANK_IMAGE['D'] = pygame.image.load('./images/tankD.gif')
    TANK_IMAGE['L'] = pygame.image.load('./images/tankL.gif')
    TANK_IMAGE['R'] = pygame.image.load('./images/tankR.gif')

    def __init__(self,_screen):
        BaseGame.__init__(self,_screen)
        self.image = Tank.TANK_IMAGE['U']
        self.rect = self.image.get_rect()  #获取图片大小
        self.rect.left = 300   #指定图片显示的X轴
        self.rect.top = 400    #指定图片显示的y轴



if __name__ == '__main__':
    tank = TankGame()
    tank.start_game()




