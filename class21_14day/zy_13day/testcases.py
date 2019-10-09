"""
============================
author:MuSen
time:2019/5/22
E-mail:3247119728@qq.com
============================
"""
import time
import unittest
from register import register


class RegisterTestCase(unittest.TestCase):

    def setUp(self):
        print('用例{}要开始执行了'.format(self))

    def tearDown(self):
        print('用例{}要开始执行结束了'.format(self))

    @classmethod
    def setUpClass(cls):
        import time
        time.sleep(2)
        print('测试用例类{}开始执行了'.format(cls))

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print('测试用例类{}执行结束了'.format(cls))

    def test_register(self):
        """正常注册"""
        # 预期结果：
        excepted = {"code": 1, "msg": "注册成功"}
        # 参数：data
        data = ('python1', '123456', '123456')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用例测试通过')

    def test_password_dis(self):
        """两次密码不一样"""
        # 预期结果：
        excepted = {"code": 0, "msg": "两次密码不一致"}
        # 参数：data
        data = ('python1', '1234567', '123456')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用例测试通过')

    def test_user_register(self):
        """账号已经被注册"""
        # 预期结果：
        excepted = {"code": 0, "msg": "该账户已存在"}
        # 参数：data
        data = ('python18', '1234567', '123456')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用例测试通过')

    def test_password_lt6(self):
        """密码长度少于6位"""
        # 预期结果：
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('python1', '12345', '12345')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用例测试通过')

    def test_password_gt18(self):
        """密码长度大于18"""
        # 预期结果：
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('python21', '1234561234561234567', '1234561234561234567')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用例测试通过')
