"""
============================
Author:柠檬班-木森
Time:2019/8/27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner


# 第一步：创建测试套件
suite = unittest.TestSuite()


# 第二步：加载测试用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(r'C:\project\python21\class21_16day\zy_15day'))



# 第三步：生成html文件的的测试报告
with open('zy_report.html', 'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            verbosity=2,
                            title='柠檬班测试报告',
                            description='这是我们21期的第一份报告作业',
                            tester='MuSen')

    runner.run(suite)


# 日志类封装 和配置文件