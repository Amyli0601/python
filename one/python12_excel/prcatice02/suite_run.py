"""
===============
author:Administrator
time:15:13
E-mail:1223607348@qq.com
===============
"""
import unittest
import cases
from cases import RegisterTestCase
from HTMLTestRunnerNew import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()
# 往测试套件里面添加用例
excepted = {"code":1,"msg":"注册成功"}
data = ('python03','123456a','123456a')
testcases = [
    {"excepted":{"code":1,"msg":"注册成功"},"data":('python03','123456a','123456a')},
    {"excepted": {"code":0,"msg":"该账户已存在"}, "data": ('python01', '123456a', '123456a')},
    {"excepted":{"code":0,"msg":"两次密码不一致"},"data":('python04','123456aa','123456a')},
    {"excepted": {"code":0,"msg":"账号和密码必须在6-18位之间"}, "data": ('python05', '12345', '12345')},
]
for case in testcases:
    suite.addTest(RegisterTestCase(case['excepted'],case['data']))
# 生成HTML测试报告
with open('report.html','wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                              verbosity=2,
                              title='HTML测试报告',
                              description = '测试',
                              tester='可乐'
                               )
    runner.run(suite)
