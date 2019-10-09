"""
===============
author:Administrator
time:16:12
E-mail:1223607348@qq.com
===============
"""
import cases
import unittest
from cases import LoginTestCase
from HTMLTestRunnerNew import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
# 方式一:添加单条用例
# suite.addTest(LoginTestCase,'test_login_pass')
# 方式二
# loader:往测试套件里面添加测试用例
loader = unittest.TestLoader()
# 添加测试用例类
suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
# # 方式三：添加模块中所有的测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(cases))
# # 方式四：通过添加路径(目录)下所有的测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.discover(r'E:\Testsoft\python.project\one\python11_unittest\unittest_practice01\testcases.py'))
# 运行测试运行程序
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 生成HTML文件的测试报告
with open('report.html','wb') as new:
    runner = HTMLTestRunner(stream=new,
                              verbosity=2,
                              title='HTML测试报告',
                              description = '测试',
                              tester='可乐'
                               )
    runner.run(suite)