"""
===============
author:Administrator
time:15:44
E-mail:1223607348@qq.com
===============
"""
# import os
# import unittest
# from interface.common.constant import DATA_DIR
# from interface.common.http_requests import HTTPSession
# from interface.common.mylog import my_log
# from interface.common.read_excel import ReadExcel
# from interface.common.read_mysql import ReadSQL
# from interface.common.test_replace import data_replace
# from interface.common.read_config import myconf
# from interface.sys_libs.ddt import ddt,data
#
# data_file_path = os.path.join(DATA_DIR,'cases.xlsx')
#
# @ddt
# class LoginTestCase(unittest.TestCase):
#     '''加标接口的测试用例类'''
#     excel = ReadExcel(data_file_path,'login')
#     cases = excel.read_cases_obj()
#     http = HTTPSession()
#     @data(*cases)
#     def test_login(self,case):
#         # 第一步：准备用例数据
#         # 替换动态化的参数
#         case.data = data_replace(case.data)
#         # 第二步：读取配置文件，发送请求，将请求内容输出日志到指定目录，获取请求结果
#         my_log.info("请求地址:{},请求接口{}，请求内容：{}".format(myconf.get('url','url')+case.url,case.interface,eval(case.data)))
#         response = self.http.request(method=case.method,url=myconf.get('url','url')+case.url,data=eval(case.data))
#         res = response.json()
#         print(res)
#         # 第三步：对比实际和预期结果
#         try:
#             self.assertEqual(str(case.excepted_code),res['code'])
#         except AssertionError as error:
#             print('测试用例不通过')
#             print('实际响应状态码为:{}'.format(res['code']))
#             print('预期响应状态码为:{}'.format(case.excepted_code))
#             self.excel.write_data(row=case.case_id+1,column=8,value='failed')
#             my_log.info('用例{}执行未通过'.format(case.title))
#             my_log.exception(error)
#             raise error
#         else:
#             print('测试用例通过')
#             print('实际响应状态码为:{}'.format(res['code']))
#             print('预期响应状态码为:{}'.format(case.excepted_code))
#             self.excel.write_data(row=case.case_id + 1, column=8, value='passed')
#             my_log.info('用例{}执行通过'.format(case.title))