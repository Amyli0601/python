"""
============================
author:LiuYu
time:2019/8/23
E-mail:253342381@qq.com
============================
"""
import unittest
from 辅导学生 import HTMLTestRunnerNew
from 辅导学生 import student_case

# suite = unittest.TestSuite()
# load = unittest.TestLoader()
suite = unittest.TestSuite()  # 测试套件
loader = unittest.TestLoader()# 用来加载用例 加载器

suite.addTest(loader.loadTestsFromModule(student_case))
# suite.addTest(loader.loadTestsFromModule(test_login))  # 运行Testadd类下面的所有用例
# suite.addTest(loader.loadTestsFromModule(test_recharge))
# suite.addTest(loader.loadTestsFromModule(test_add))
# suite.addTest(loader.loadTestsFromModule(test_withdraw))
with open("text.html", "wb") as file:  #创建一个文件存储测试报告
      runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                verbosity=2,
                                                title="接口自动化测试报告",
                                                description="2019.4.4测试报告",
                                                tester="路人")
      runner.run(suite) #执行测试套间里面的用例
# suite.addTest(load.discover(r'D:\python_21\test_student'))


# with open('regist.html','wb') as d:
#     runner = HTMLTestRunner(stream=d,
#                             verbosity=2,
#                             title='注册的测试报告',
#                             description='这是我们21期的一份测试报告',
#                             tester='liuyu')
#     runner.run(suite)
