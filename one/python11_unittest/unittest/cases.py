"""
===============
author:Administrator
time:15:00
E-mail:1223607348@qq.com
===============
"""
import unittest
from register import register_check
class RegisterTestCase(unittest.TestCase):
    """测试登录功能函数的测试用例类"""
    def setUp(self):
        print('用例{}开始执行'.format(self))
    def tearDown(self):
        print('用例{}执行结束'.format(self))
    def test_register_pass(self):
        '''注册成功的用例'''
        # 入参
        username = 'lucky01'
        pwd1 = '123456a'
        pwd2 = '123456a'
        # 预期结果
        excepted01 = {"code":1,"msg":"注册成功"}
        # 执行功能函数，获取实际结果
        user = register_check(username,pwd1,pwd2)
        try:
            # 对比预期结果和实际结果
            self.assertEqual(excepted01,user)
        except AssertionError as a:
            print('测试用例不通过')
            print('预期结果：{}'.format(excepted01))
            print('实际结果：{}'.format(user))
            raise a
        else:
            print('测试用例通过')
            print('预期结果：{}'.format(excepted01))
            print('实际结果：{}'.format(user))

    def test_register_failed(self):
        '''账号已存在的测试用例'''
        # 入参
        username = 'python01'
        pwd1 = '123456a'
        pwd2 = '123456a'
        # 预期结果
        excepted01 = {"code":0,"msg":"该账户已存在"}
        # 执行功能函数，获取实际结果
        user = register_check(username, pwd1, pwd2)
        try:
            # 对比预期结果和实际结果
            self.assertEqual(excepted01, user)
        except AssertionError as a:
            print('测试用例不通过')
            print('预期结果：{}'.format(excepted01))
            print('实际结果：{}'.format(user))
            raise a
        else:
            print('测试用例通过')
            print('预期结果：{}'.format(excepted01))
            print('实际结果：{}'.format(user))
    def test_password_different(self):
        '''密码不一致的测试用例'''
        # 入参
        username = 'amy'
        pwd1 = '123456a'
        pwd2 = '123456'
        # 预期结果
        excepted01 = {"code":0,"msg":"两次密码不一致"}
        # 执行功能函数，获取实际结果
        user = register_check(username, pwd1, pwd2)
        try:
            # 对比预期结果和实际结果
            self.assertEqual(excepted01, user)
        except AssertionError as a:
            print('测试用例不通过')
            print('预期结果：{}'.format(excepted01))
            print('实际结果：{}'.format(user))
            raise a
        else:
            print('测试用例通过')
            print('预期结果：{}'.format(excepted01))
            print('实际结果：{}'.format(user))

    def test_password_outlen6(self):
        '''密码小于6位的用例'''
        # 入参
        username = 'amy'
        pwd1 = '1234'
        pwd2 = '1234'
        # 预期结果
        excepted01 = {"code":0,"msg":"账号和密码必须在6-18位之间"}
        # 执行功能函数，获取实际结果
        user = register_check(username, pwd1, pwd2)
        try:
            # 对比预期结果和实际结果
            self.assertEqual(excepted01, user)
        except AssertionError as a:
            print('测试用例不通过')
            print('预期结果：{}'.format(excepted01))
            print('实际结果：{}'.format(user))
            raise a
        else:
            print('测试用例通过')
            print('预期结果：{}'.format(excepted01))
            print('实际结果：{}'.format(user))
    def test_password_outlen18(self):
        '''密码超过18位的用例'''
        # 入参
        username = 'amy'
        pwd1 = '12345678901234567890'
        pwd2 = '12345678901234567890'
        # 预期结果
        excepted01 = {"code":0,"msg":"账号和密码必须在6-18位之间"}
        # 执行功能函数，获取实际结果
        user = register_check(username, pwd1, pwd2)
        try:
            # 对比预期结果和实际结果
            self.assertEqual(excepted01, user)
        except AssertionError as a:
            print('测试用例不通过')
            print('预期结果：{}'.format(excepted01))
            print('实际结果：{}'.format(user))
            raise a
        else:
            print('测试用例通过')
            print('预期结果：{}'.format(excepted01))
            print('实际结果：{}'.format(user))