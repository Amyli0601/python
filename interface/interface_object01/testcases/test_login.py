"""
===============
author:Administrator
time:17:01
E-mail:1223607348@qq.com
===============
"""
'''
测试用例模块
'''
import unittest
from ddt import ddt,data
from interface_object01.common.read_excel import ReadExcel
from interface_object01.common.http_requests import HTTPRequest
from interface_object01.common.mylog import my_log

@ddt
class LoginTestCase(unittest.TestCase):
    # 登录接口的测试用例
    excel = ReadExcel(r'E:\Testsoft\python.project\interface\interface_object01\datas\cases.xlsx','login')
    cases = excel.read_cases_obj()
    http = HTTPRequest()
    @data(*cases)
    def test_case_login(self,case):
        '''登录接口用例执行逻辑'''
        # 第一步：准备测试用例数据
        url = case.url
        data = eval(case.data)
        method = case.method
        excepted = eval(case.excepted)
        # 第二步：发送请求到接口，获取响应结果
        my_log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method,url=url,data=data)
        # 获取响应json内容
        res = response.json()
        # 第三步：对比实际和预期结果，断言是否测试通过
        try:
            self.assertEqual(excepted,res)
        except AssertionError as error:
            print('测试用例不通过')
            print('预期结果为：{}'.format(excepted))
            print('实际结果为：{}'.format(res))
            self.excel.write_data(case.case_id+1,8,'failed')
            my_log.debug('{}用例执行未通过'.format(case.title))

            raise error
        else:
            print('测试用例通过')
            print('预期结果为：{}'.format(excepted))
            print('实际结果为：{}'.format(res))
            self.excel.write_data(case.case_id+1,8,'passed')
            my_log.debug('{}用例执行通过'.format(case.title))
