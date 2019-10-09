"""
===============
author:Administrator
time:13:51
E-mail:1223607348@qq.com
===============
"""
import unittest
from login import login_check
class LoginTestCase(unittest.TestCase):
    '''测试用例类必须继承于TestCase'''
    # 用例功能函数执行开始前执行
    def setUp(self):
        print('用例{}开始执行'.format(self))
    # 用例功能函数执行结束后执行
    def tearDown(self):
        print('用例{}结束执行'.format(self))
    # 测试用例类执行开始前执行
    @classmethod
    def setUpClass(cls):
        print('测试用例类{}开始执行'.format(cls))
    # 测试用例类执行结束后执行
    @classmethod
    def tearDownClass(cls):
        print('测试用例类{}结束执行'.format(cls))
    # 创建测试用例类
    def test_login_pass(self):
        '''正常登录的用例'''
        # 预期结果
        excepted = {"code":200,"msg":"登录成功"}
        # 实际结果
        res = login_check('Amy00001','123456a')
        # 对比预期和实际结果
        try:
            self.assertEqual(excepted,res)
        except AssertionError as error:
            print('该条用例执行未通过')
            print('实际结果为:{}'.format(res))
            print('预期结果为:{}'.format(excepted))
            raise error
        else:
            print('该条用例执行通过')
            print('实际结果为:{}'.format(res))
            print('预期结果为:{}'.format(excepted))
    def test_login_pwd_error(self):
        excepted = {"code":999,"msg":"证号或密码不正确"}
        res =login_check('Amy00001','123456aa')
        try:
            self.assertEqual(excepted,res)
        except AssertionError as error:
            print('该条用例执行未通过')
            print('实际结果为:{}'.format(res))
            print('预期结果为:{}'.format(excepted))
            raise error
        else:
            print('该条用例执行通过')
            print('实际结果为:{}'.format(res))
            print('预期结果为:{}'.format(excepted))
    def test_login_user_error(self):
        excepted = {"code":999,"msg":"证号或密码不正确"}
        res = login_check('Amy001','123456a')
        try:
            self.assertEqual(excepted,res)
        except AssertionError as error:
            print('该条用例执行未通过')
            print('实际结果为:{}'.format(res))
            print('预期结果为:{}'.format(excepted))
            raise error
        else:
            print('该条用例执行通过')
            print('实际结果为:{}'.format(res))
            print('预期结果为:{}'.format(excepted))
    def test_login_ped_less6(self):
        excepted = {"code":999,"msg":"密码长度在6-18位之间"}
        res = login_check('Amy00001', '123456')
        try:
            self.assertEqual(excepted,res)
        except AssertionError as error:
            print('该条用例执行未通过')
            print('实际结果为:{}'.format(res))
            print('预期结果为:{}'.format(excepted))
            raise error
        else:
            print('该条用例执行通过')
            print('实际结果为:{}'.format(res))
            print('预期结果为:{}'.format(excepted))