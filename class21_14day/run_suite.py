"""
============================
Author:柠檬班-木森
Time:2019/8/19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from testcases import RegisterTestCase

# 创建测试套件
suite = unittest.TestSuite()

# 加载用例到套件


cases = [
    {"excepted": {"code": 1, "msg": "注册成功"}, "data": ('python1', '123456', '123456')},
    {"excepted": {"code": 0, "msg": "两次密码不一致"}, "data": ('python1', '1234567', '123456')},
    {"excepted": {"code": 0, "msg": "该账户已存在"}, "data": ('python18', '1234567', '123456')}
]
"""
[
{'case_id': 1, 'data': "('python1', '123456', '123456')", 'excepted': '{"code": 1, "msg": "注册成功"}'}, 
{'case_id': 2, 'data': "('python1', '1234567', '123456')", 'excepted': '{"code": 0, "msg": "两次密码不一致"}'}, 
{'case_id': 3, 'data': "('python18', '1234567', '123456')", 'excepted': '{"code": 0, "msg": "该账户已存在"}'}
]

"""


for case in cases:
    suite.addTest(RegisterTestCase('test_register',case["excepted"], case["data"]))


# 生成html文件的的测试报告

with open('zy_report.html', 'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            verbosity=2,
                            title='柠檬班测试报告',
                            description='这是我们21期的第一份报告作业',
                            tester='MuSen')

    runner.run(suite)
