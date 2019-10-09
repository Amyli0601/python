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
import os
import unittest
from interface_object03.common.mylog import my_log
from interface_object03.sys_libs.ddt import ddt,data
from interface_object03.common.constant import DATA_DIR
from interface_object03.common.read_config import myconf
from interface_object03.common.read_excel import ReadExcel
from interface_object03.common.test_replace import data_replace
from interface_object03.common.http_requests import HTTPRequest



@ddt
class LoginTestCase(unittest.TestCase):
    """登录接口的测试用例"""
    # 拼接读取用例数据的路径，为ReadExcel创建一个对象
    excel = ReadExcel(os.path.join(DATA_DIR,'cases.xlsx'),'login')
    # 用ReadExcel类的实例对象调取类中的方法
    cases = excel.read_cases_obj()
    http = HTTPRequest()
    @data(*cases)
    def test_case_login(self,case):
        '''登录接口用例执行逻辑'''
        # 第一步：准备测试用例数据
        url = myconf.get('url','url')+case.url
        method = case.method
        excepted = eval(case.excepted)
        # 替换要格式化的用例参数
        data = data_replace(case.data)
        # print(data,type(data))
        # 第二步：读取配置文件，发送请求，将请求内容输出日志到指定目录，获取请求结果
        my_log.info('请求地址{},请求接口{},请求内容:{}'.format(url,case.interface,data))
        response = self.http.request(method=method,url=url,data=eval(data))
        res = response.json()
        # 第三步：对比实际和预期结果，断言是否测试通过
        try:
            self.assertEqual(excepted,res)
            # if case.check_sql:
            #     case.check_sql=case.check_sql.replace('#phone#',myconf.get('data','phone'))
            #     db_res = self.db.find_count(case.check_sql)
            #     self.assertEqual(1,db_res)
        except AssertionError as error:
            print('测试用例不通过')
            print('预期结果为:{}'.format(excepted))
            print('实际结果为:{}'.format(res))
            # 将断言结果写入测试数据中
            self.excel.write_data(case.case_id+1,8,'failed')
            # 将执行的测试用例title输出到日志
            my_log.debug('{}用例执行未通过'.format(case.title))
            raise error
        else:
            print('测试用例通过')
            print('预期结果为:{}'.format(excepted))
            print('实际结果为:{}'.format(res))
            # 将断言结果写入测试数据中
            self.excel.write_data(case.case_id+1,8,'passed')
            # 将执行的测试用例title输出到日志
            my_log.debug('{}用例执行通过'.format(case.title))
