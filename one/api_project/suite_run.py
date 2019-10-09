"""
===============
author:Administrator
time:15:13
E-mail:1223607348@qq.com
===============
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner

# 1、创建测试套件
suite = unittest.TestSuite()
# 2、加载测试用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(r'E:\Testsoft\python.project\one\python15_object\testcases'))
# 3、生成HTML测试报告
with open(r'E:\Testsoft\python.project\one\python15_object\reports\report.HTML','wb') as new:
    runner = HTMLTestRunner(stream=new,
                              verbosity=2,
                              title='HTML测试报告',
                              description = '测试',
                              tester='可乐'
                               )
    runner.run(suite)
