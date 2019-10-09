"""
===============
author:Administrator
time:12:16
E-mail:1223607348@qq.com
===============
"""
from HTMLTestRunnerNew import HTMLTestRunner
import  unittest
from  testcases import LoginTestCase
import  testcases
# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到套件
# 方式一 添加单条用例
# suite.addTest(LoginTestCase,'test_login_case_pass')
# 方式二 添加测试用例类的所有用例
# 往测试套件中加载测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
# #方式三 添加一个模块所有的测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))
# 方式四 添加路径（目录）下所有测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.discover(''))
# print(suite)

# 创建测试运行程序，执行测试用例
# runner = unittest.TextTestRunner
# runner.run(suite)

# 生成HTML测试报告
with open('report.html','wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                              verbosity=2,
                              title='unitest测试报告01',
                              description = '测试',
                              tester='可乐'
                               )
    runner.run(suite)