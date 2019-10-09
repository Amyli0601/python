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
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(cases))
# 生成HTML测试报告
with open('report.html','wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                              verbosity=2,
                              title='单元测试报告01',
                              description = '测试',
                              tester='可乐'
                               )
    runner.run(suite)
