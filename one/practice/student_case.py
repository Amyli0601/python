"""
============================
author:LiuYu
time:2019/8/23
E-mail:253342381@qq.com
============================
"""
import unittest
from ddt import ddt,data
from 辅导学生.start_file import register as f
from 辅导学生.student_excel import DoExcsl


@ddt
class  TestRunnner(unittest.TestCase):
    excel = DoExcsl('case.xlsx','liuyu')
    cases = excel.login_excel()

    # def __init__(self,expect,cell):
    #     super().__init__('test_pass')
    #     self.expect = expect
    #     self.cell =cell
    @data(*cases)
    def test_pass(self,case):
        print(case)
        # if type(eval(case)) == 'dict' :

        expect = f(eval(case['Params'])['user'],eval(case['Params'])['pwd'],eval(case['Params'])['pwd1']) # 实际结果
        cell = eval(case['cell'])     # 预期结果
        # data =f(*cell)
        try:
            self.assertEqual(expect,cell)
        except AssertionError as e:
            print('该条用例执行未通过')
            self.excel.write_excel(case.number + 1,4,'no')
            raise e
        else:
            print('该条用例执行通过', '预期结果：{}'.format(expect), '实际结果：{}'.format(cell))
            self.excel.write_excel(case.number + 1, 4, 'yes')





