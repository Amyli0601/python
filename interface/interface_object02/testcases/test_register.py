"""
===============
author:Administrator
time:16:50
E-mail:1223607348@qq.com
===============
"""
import os
import unittest
from interface_object02.sys_libs.ddt import ddt,data
from interface_object02.common.read_excel import ReadExcel
from interface_object02.common.constant import DATA_DIR
from interface_object02.common.http_requests import HTTPRequest
from interface_object02.common.mylog import my_log

@ddt
class RegisterTestCase(unittest.TestCase):
    '''注册模块的测试用例类'''
    excel = ReadExcel(os.path.join(DATA_DIR,'cases.xlsx'),'register')
    cases =excel.read_cases_obj()
    http = HTTPRequest()
    @data(*cases)
    def test_case_register(self,case):
        '''注册模块的用例执行逻辑'''
        # 第一步：准备测试用例数据
        title = case.title
        url =case.url
        method = case.method
        data =eval( case.data)
        excepted = eval(case.excepted)
        # 第二步：准备发送请求，读取配置文件将日志输出到指定目录，并获取响应结果
        my_log.info('请求地址:{}'.format(url))
        response = self.http.request(method,url,data)
        res = response.json()
        # 第三步：对比预期和实际结果
        try:
            self.assertEqual(excepted,res)
        except AssertionError as error:
            print('用例测试不通过')
            print('预期结果为:{}'.format(excepted))
            print('实际结果为:{}'.format(res))
            self.excel.write_data(case.case_id+1,8,'failed')
            my_log.debug('用例:{}测试不通过'.format(title))
            raise error
        else:
            print('用例测试通过')
            print('预期结果为:{}'.format(excepted))
            print('实际结果为:{}'.format(res))
            self.excel.write_data(case.case_id+1,8,'passed')
            my_log.debug('用例:{}测试通过'.format(title))




