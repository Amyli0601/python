"""
===============
author:Administrator
time:18:07
E-mail:1223607348@qq.com
===============
"""
import os
import decimal
import unittest
from interface.common.mylog import my_log
from interface.sys_libs.ddt import ddt,data
from interface.common.read_mysql import ReadSQL
from interface.common.constant import DATA_DIR
from interface.common.read_config import myconf
from interface.common.read_excel import ReadExcel
from interface.common.http_requests import HTTPSession,HTTPRequest
from interface.common.test_replace import data_replace


data_file_path = os.path.join(DATA_DIR,'cases.xlsx')

@ddt
class RechargeTestCase(unittest.TestCase):
    '''充值接口的测试用例类'''
    excel = ReadExcel(data_file_path,'product')
    cases = excel.read_cases_obj()
    http = HTTPRequest()
    db = ReadSQL()
    @data(*cases)
    def test_PRODCUT(self,case):
        # 第一步：准备用例数据
        url = myconf.get('url','url')+case.url
        interface = case.interface
        method = case.method
        # 替换动态化的参数
        if "#sessionId#" in case.data:
            # 将需要格式化的字符串提取出来，替换为格式化的参数
            data = eval(case.data.replace('#sessionId#', myconf.get('user', 'sessionId')))


        # 第二步：读取配置文件，发送请求，将请求内容输出日志到指定目录，获取请求结果
        my_log.info("请求地址:{},请求接口{}，请求内容：{}".format(url,interface,data))
        response = self.http.request(method,url=url,data=data)
        res = response.json()
        # 第三步：对比实际和预期结果
        try:
            self.assertEqual(str(case.excepted_code),res['code'])
            if case.check_sql:
                # 将需要格式化的字符串提取出来，替换为格式化的参数
                case.check_sql = case.check_sql.replace('#distributer_no#',myconf.get('user','distributer_no'))
                # 获取当前分销商产品总数
                product_count = self.db.fetchone(case.check_sql)[0]
                print(product_count)
                # 对比实际分销商产品总数和预期
                self.assertEqual(3,product_count)
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