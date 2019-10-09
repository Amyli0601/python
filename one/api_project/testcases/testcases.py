"""
===============
author:Administrator
time:15:00
E-mail:1223607348@qq.com
===============
'''
ddt:数据驱动思想
@ddt:装饰器
'''
"""
import unittest
from ddt import ddt,data
from python15_object.common.register import register_check
from python15_object.common.read_excel import ReadExcel
# 读取测试用例
@ddt
class RegisterTestCase(unittest.TestCase):
    """测试登录功能函数的测试用例类"""
    # cases = ReadExcel('cases.xlsx', 'cases').read_cases_obj()
    excel = ReadExcel(r'E:\Testsoft\python.project\one\python15_object\datas\cases.xlsx', 'cases')
    cases = excel.read_cases_obj()
    def setUp(self):
        print('用例{}开始执行'.format(self))
    def tearDown(self):
        print('用例{}执行结束'.format(self))
    @data(*cases)
    def test_register(self,case):
    #     '''注册模块的用例'''
        # 预期结果
        excepted = eval(case.excepted)
        # print(excepted)
        # 入参参数data
        data = eval(case.data)
        # print(data)
        # 执行功能函数，获取实际结果
        res = register_check(*data)
        try:
            # 对比预期结果和实际结果
            self.assertEqual(excepted,res)
        except AssertionError as error:
            print('测试用例不通过')
            self.excel.write_data(case.case_id+1,4,'failed')
            print('预期结果：{}'.format(excepted))
            print('实际结果：{}'.format(res))
            raise error
        else:
            print('测试用例通过')
            self.excel.write_data(case.case_id+1, 4, 'passed')
            print('预期结果：{}'.format(excepted))
            print('实际结果：{}'.format(res))
