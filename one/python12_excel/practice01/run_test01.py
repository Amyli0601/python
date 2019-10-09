"""
===============
author:Administrator
time:15:26
E-mail:1223607348@qq.com
===============
"""
import unittest
import test_cases01
from test_cases01 import RegisterTestCase
from HTMLTestRunnerNew import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()
# 往测试套件里面添加用例
loader = unittest.TestLoader()
mycases = [
    {'excepted':{"code":1,"msg":"注册成功"},'data':('lucky01','123456a','123456a')},
    {'excepted':{"code":0,"msg":"该账户已存在"},'data':('python01','123456a','123456a')},
    {'excepted':{"code":0,"msg":"两次密码不一致"},'data':('lucky01','123456a','123456')},
    {'excepted':{"code":0,"msg":"账号和密码必须在6-18位之间"},'data':('lucky01','1234','1234')},
    {'excepted':{"code":0,"msg":"账号和密码必须在6-18位之间"},
     'data':('lucky01','1234567890123456789','1234567890123456789')}
]
for case in mycases:
    suite.addTest(RegisterTestCase(case['excepted'],case['data']))

# 生成HTML测试报告
with open('report.html','wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                              verbosity=2,
                              title='单元测试报告02',
                              description = '测试',
                              tester='可乐'
                               )
    runner.run(suite)