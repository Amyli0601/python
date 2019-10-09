"""
============================
author:MuSen
time:2019/5/22
E-mail:3247119728@qq.com
============================
"""
import unittest
from register import register


class RegisterTestCase(unittest.TestCase):

    def setUp(self):
        print('用例{}要开始执行了'.format(self))

    def tearDown(self):
        print('用例{}要开始执行结束了'.format(self))

    def __init__(self, methodname,excepted, data):
        super().__init__(methodname)
        self.excepted = eval(excepted)
        self.data = eval(data)


    def test_register(self):
        """正常注册"""
        # 预期结果：
        excepted = self.excepted
        # 参数：data
        data = self.data
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用例测试通过')

