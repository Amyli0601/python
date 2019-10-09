"""
===============
author:Administrator
time:15:44
E-mail:1223607348@qq.com
===============
"""
import os
import decimal
import unittest
from interface_object03.common.mylog import my_log
from interface_object03.sys_libs.ddt import ddt,data
from interface_object03.common.read_mysql import ReadSQL
from interface_object03.common.constant import DATA_DIR
from interface_object03.common.read_config import myconf
from interface_object03.common.read_excel import ReadExcel
from interface_object03.common.http_requests import HTTPSession
from interface_object03.common.test_replace import data_replace



# data_file_path = os.path.join(DATA_DIR, 'cases.xlsx')

# @ddt
# class AddTestCase(unittest.TestCase):
#     """加标接口"""
#     excel = ReadExcel(data_file_path, 'add')
#     cases = excel.read_cases_obj()
#     http = HTTPSession()
#     db = ReadSQL()
#
#     @data(*cases)
#     def test_add(self, case):
#         # 第一步：准备用例数据
#         # 拼接接口路径
#         case.url = myconf.get('url','url')+case.url
#         # 替换用例参数
#         case.data = data_replace(case.data)
#
#         if "*memberId*" in case.data:
#             max_id = self.db.fetchone("SELECT max(id) FROM member")[0]
#             memberid = max_id+1
#             case.data = case.data.replace("*memberId*",str(memberid))
#         # 判断是否需要sql校验
#         if case.check_sql:
#             case.check_sql = data_replace(case.check_sql)
#             # 获取当前用户加标前的标数量
#             start_count = self.db.find_count(case.check_sql)
#
#         # 第二步 发送请求，获取结果
#         my_log.info("请求地址:{},请求接口{}，请求内容：{}".format(myconf.get('url','url')+case.url,case.interface,eval(case.data)))
#         response = self.http.request(method=case.method, url=case.url, data=eval(case.data))
#         res = response.json()
#         res_code = res['code']
#         # 第三步 比对预期和实际结果
#         try:
#             self.assertEqual(str(case.excepted_code), res_code)
#             if case.check_sql:
#                 # 获取当前用户加标之后的标数量
#                 end_count = self.db.find_count(case.check_sql)
#                 self.assertEqual(1,end_count-start_count)
#         except AssertionError as e:
#             # 用例执行未通过
#             self.excel.write_data(row=case.case_id + 1, column=8, value='failed')
#             my_log.info('{}:用例执行未通过'.format(case.title))
#             my_log.exception(e)
#             raise e
#         else:
#             # 用例执行通过
#             self.excel.write_data(row=case.case_id + 1, column=8, value='passed')
#             my_log.info('{}:用例执行通过'.format(case.title))
#

#
#
data_file_path = os.path.join(DATA_DIR,'cases.xlsx')

@ddt
class AddTestCase(unittest.TestCase):
    '''加标接口的测试用例类'''
    excel = ReadExcel(data_file_path,'add')
    cases = excel.read_cases_obj()
    http = HTTPSession()
    db = ReadSQL()
    @data(*cases)
    def test_add(self,case):
        # 第一步：准备用例数据
        # 替换动态化的参数
        case.data = data_replace(case.data)
        # 判断用例数据中是否有需要动态化的参数
        if '*memberId*' in case.data:
            # 获取数据库用户表当前最大的会员id
            max_id = self.db.fetchone("select max(id) from member")[0]
            # 将要加标的新会员id
            memberId = max_id+1
            # 替换用例数据中的会员id
            case.data = case.data.replace('*memberId*',str(memberId))

        # 判断是否需要sql校验
        if case.check_sql:
            case.check_sql = data_replace(case.check_sql)
            # 获取当前用户加标前的标数量
            start_count = self.db.find_count(case.check_sql)

        # 第二步：读取配置文件，发送请求，将请求内容输出日志到指定目录，获取请求结果
        my_log.info("请求地址:{},请求接口{}，请求内容：{}".format(myconf.get('url','url')+case.url,case.interface,eval(case.data)))
        response = self.http.request(method=case.method,url=myconf.get('url','url')+case.url,data=eval(case.data))
        res = response.json()
        # 第三步：对比实际和预期结果
        try:
            self.assertEqual(str(case.excepted_code),res['code'])
            if case.check_sql:
                # 获取加标之后的当前用户的标数量
                end_count = self.db.find_count(case.check_sql)
                self.assertEqual(1,end_count - start_count)

        except AssertionError as error:
            print('测试用例不通过')
            print('实际响应状态码为:{}'.format(res['code']))
            print('预期响应状态码为:{}'.format(case.excepted_code))
            self.excel.write_data(row=case.case_id+1,column=8,value='failed')
            my_log.info('用例{}执行未通过'.format(case.title))
            my_log.exception(error)
            raise error
        else:
            print('测试用例通过')
            print('实际响应状态码为:{}'.format(res['code']))
            print('预期响应状态码为:{}'.format(case.excepted_code))
            self.excel.write_data(row=case.case_id + 1, column=8, value='passed')
            my_log.info('用例{}执行通过'.format(case.title))