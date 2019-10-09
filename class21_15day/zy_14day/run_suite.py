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
from read_excel import ReadExcel
# 第一步：创建测试套件
suite = unittest.TestSuite()



# 第二步：读取测试用例
cases = ReadExcel('cases.xlsx','Sheet1').read_data()


# 第三步：加载用例到套件
for case in cases:
    suite.addTest(RegisterTestCase('test_register',case["excepted"], case["data"]))


# 第四步：生成html文件的的测试报告
with open('zy_report.html', 'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            verbosity=2,
                            title='柠檬班测试报告',
                            description='这是我们21期的第一份报告作业',
                            tester='MuSen')

    runner.run(suite)