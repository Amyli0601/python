"""
===============
author:Administrator
time:15:13
E-mail:1223607348@qq.com
===============
"""
import unittest
import cases
from read_excel_obj import ReadExcel,CaseData
from cases import RegisterTestCase
from HTMLTestRunnerNew import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()
# 读取测试用例
cases = ReadExcel('cases.xlsx','cases').read_cases()
# 往测试套件里面添加用例
for case in cases:
    suite.addTest(RegisterTestCase('test_register',case['excepted'],case['data']))
# 生成HTML测试报告
with open('report02.html','wb') as new:
    runner = HTMLTestRunner(stream=new,
                              verbosity=2,
                              title='HTML测试报告02',
                              description = '测试',
                              tester='可乐'
                               )
    runner.run(suite)
