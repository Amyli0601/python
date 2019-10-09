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
    def __init__(self,excepted,data):
        super().__init__('test_register')
        self.excepted = excepted
        self.data = data
    def test_register(self):
        '''注册模块的用例'''
        # 预期结果
        excepted = self.excepted
        # 入参参数data
        data = self.data
        # 执行功能函数，获取实际结果
        res = register_check(*data)
        try:
            # 对比预期结果和实际结果
            self.assertEqual(excepted,res)
        except AssertionError as a:
            print('测试用例不通过')
            print('预期结果：{}'.format(excepted))
            print('实际结果：{}'.format(res))
            raise a
        else:
            print('测试用例通过')
            print('预期结果：{}'.format(excepted))
            print('实际结果：{}'.format(res))
