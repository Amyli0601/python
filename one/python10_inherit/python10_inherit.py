"""
===============
author:Administrator
time:14:39
E-mail:1223607348@qq.com
===============
"""

# class  Web_Page:
#     def __init__(self,url,request,expect,reality):
#         self.url = url
#         self.request = request
#         self.expect = expect
#         self.reality = reality
# # 用类创建对象
# user_test1 = Web_Page('http://47.92.107.201/compensate-api/progress',
#                       '{"report_info": {}}','passed','passed')
# user_test2 = Web_Page('http://47.92.107.201/compensate-api/progress',
#                       '{"report_info": {}}','failed','failed')
#
# # 利用反射机制，获取方法
# res1 = getattr(user_test1,'url')
# print(res1)
# # 获取对象属性
# setattr(user_test1,'result','ok')
# print(user_test1.result)
# # 删除对象属性
# delattr(user_test1,'result')
# print(user_test1.result)
#
# 2、将上课写的手机（v1-v3）类定义好，在这个基础上再定义一个安卓手机类（V41），苹果手机类（V42）,这两个手机
#  类都继承于V3版手机类。
# V41：新增的方法：拍照、谷歌应用商店
# V42：新增功能：苹果应用商店 语言助手sir

# class Phone_v1(object):
#     attr1 = '打电话'
#     def call_phone(self):
#         print('这个是打电话的功能')
# v1 = Phone_v1()
# class Phone_v2(Phone_v1):
#     def send_msg(self):
#         print('这个是发短信的功能')
#     def play_music(self):
#         print('播放音乐')
# v2 = Phone_v2()
# class Phone_v3(Phone_v2):
#     def play_video(self):
#         print('播放视频')
# v3 = Phone_v3()
# class Android(Phone_v3):
#     def photo(self):
#         print('拍照功能')
#     def geogle_store(self):
#         print('谷歌应用商店')
# android = Android()
# class Ios(Phone_v3):
#     def iPhone_store(self):
#         print('苹果应用商店')
#     def voice_assistant(self):
#         print('语音助手')
# ios = Ios()
# android.play_video()
# ios.play_video()
import  random
class BaseTank(object):
    def __init__(self): # 初始化实例对象属性
        self.live = 1
        self.postion = random.randint(1,10)
        self.hp = 10
        self.attack_postion = random.randint(1,10)
class MyTank(BaseTank):
    def move(self):
        while True:
            try:
                target_postion = int(input('请输入移动的目标位置：'))
            except ValueError:
                print('您输入的数据无效,请重新输入')
            else:
                if 1<=target_postion <=10:
                    self.postion = target_postion
                    break
                else:
                    print('您输入的数据无效,请重新输入')
    def Bullet_launch(self):
        while True:
            try:
                attack_postion = int(input('请输入攻击位置：'))
            except ValueError:
                print('您输入的数据无效,请重新输入')
            else:
                if attack_postion >=1 and attack_postion <=10:
                    self.attack_postion = attack_postion
                    break
                else:
                    print('您输入的数据无效,请重新输入')
class PCTank(BaseTank):
    def move(self):
        self.postion = random.randint(1,10)
    def billet_lanuch(self):
        self.attack_postion = random.randint(1,10)
def game():
    me = MyTank()
    pc = PCTank()
    while True:
        me.Bullet_launch()
        pc.billet_lanuch()
        if me.attack_postion == pc.postion:
            pc.hp-=1
        elif pc.attack_postion == me.postion:
            me.hp-=1
        elif pc.hp==0 and me.hp==0:
            print('双方阵亡，游戏结束')
            break
        elif pc.hp== 0 and 0<me.hp <=10:
            print('电脑玩家阵亡，您胜利了')
            break
        elif me.hp==0 and 0<pc.hp<=10:
            print('您输了')
            break
        me.move()
        pc.move()
game()













