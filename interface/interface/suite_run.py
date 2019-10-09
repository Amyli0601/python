"""
===============
author:Administrator
time:15:13
E-mail:1223607348@qq.com
===============
"""
'''
项目启动文件
'''
import os
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from interface.common.constant import CASE_DIR, REPORT_DIR
from interface.common.mylog import my_log
from interface.common.read_config import myconf

# 项目开始时输出日志
my_log.info("------开始执行测试运行程序------")

# 第一步：创建测试套件
suite = unittest.TestSuite()

# 第二步：将用例添加到测试套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))
# 第三步：执行用例，生成测试报告
# 从配置文件中读取测试报告的名称，并和路径拼接生成一个指定路径指定名称的测试报告
file_name = myconf.get('report','file_name')
report = os.path.join(REPORT_DIR,file_name)
with open(report,'wb') as new:
    runner = HTMLTestRunner(
                            stream=new,
                            verbosity=2,
                            title='report01',
                            description='接口测试报告',
                            tester='可乐'
                            )
    runner.run(suite)

# 用例执行结束输入日志
my_log.info('------用例执行结束------')