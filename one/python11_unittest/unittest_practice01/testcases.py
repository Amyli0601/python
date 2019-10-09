"""
===============
author:Administrator
time:10:51
E-mail:1223607348@qq.com
===============
"""
import unittest
from login import login_check
class LoginTestCase(unittest.TestCase):
    """测试用例类必须继承于TestCase
    测试登录模块的测试用例类"""
    # 创建测试用例，必须是以test开头的方法
    def test_login_case_pass(self):
        """正常登录的用例"""
        # 预期结果
        excepted1 = {"code":200,"msg":"登录成功"}
        # 执行功能函数，获取实际结果
        res1 = login_check('python21','123456a')
        # 对比预期和实际结果
        try:
            self.assertEqual(excepted1,res1)
        except AssertionError as e:
            print('用例不通过')
            print('预期结果：{}'.format(excepted1))
            print('实际结果：{}'.format(res1))
            raise e
        else:
            print('用例通过')
            print('预期结果：{}'.format(excepted1))
            print('实际结果：{}'.format(res1))

    def test_login_case_error(self):
        """密码错误的用例"""
        # 创建测试用例，必须是以test开头的方法
        # 准备测试用例数据
        # 入参
        username = 'python21'
        pwd = '123'
        # 预期的结果
        excepted2 = {"code":999,"msg":"证号或密码不正确"}
        # 执行功能函数，获取实际结果
        res2 = login_check(username,pwd)
        # 对比预期和实际结果
        try:
            self.assertEqual(excepted2,res2)
        except AssertionError as e:
            print('用例不通过')
            print('预期结果：{}'.format(excepted2))
            print('实际结果：{}'.format(res2))
            raise e
        else:
            print('用例通过')
            print('预期结果：{}'.format(excepted2))
            print('实际结果：{}'.format(res2))
