"""
============================
author:MuSen
time:2019/5/22
E-mail:3247119728@qq.com
============================
"""
import unittest
from register import register
from ddt import ddt, data
from read_excel import ReadExcel





@ddt
class RegisterTestCase(unittest.TestCase):
    excel = ReadExcel('cases.xlsx', 'Sheet1')
    # cases = excel.read_data()
    cases = excel.read_data_obj()

    def setUp(self):
        print('用例{}要开始执行了'.format(self))

    def tearDown(self):
        print('用例{}要开始执行结束了'.format(self))

    @data(*cases)
    def test_register(self, case):
        """正常注册"""
        # 预期结果：
        excepted = eval(case.excepted)
        # 参数：data
        data = eval(case.data)
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            # 回写结果到excel文件中
            self.excel.write_data(case.case_id + 1, 4, '未通过')
            raise e
        else:
            print('该用例测试通过')
            # 回写结果到excel文件中
            self.excel.write_data(case.case_id + 1, 4, '通过')

    # @data(*cases)
    # def test_register(self, case):
    #     """正常注册"""
    #     # 预期结果：
    #     excepted = eval(case['excepted'])
    #     # 参数：data
    #     data = eval(case['data'])
    #     # 调用被测试的功能函数，传入参数，获取实际结果：
    #     res = register(*data)
    #     try:
    #         self.assertEqual(excepted, res)
    #     except AssertionError as e:
    #         print('该用例测试未通过')
    #         self.excel.write_data(case['case_id']+1, 4, '未通过')
    #         raise e
    #     else:
    #         print('该用例测试通过')
    #         self.excel.write_data(case['case_id']+1, 4, '通过')
