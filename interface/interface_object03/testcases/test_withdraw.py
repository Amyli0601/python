"""
===============
author:Administrator
time:17:11
E-mail:1223607348@qq.com
===============
"""
import os
import decimal
import unittest
from interface_object03.common.mylog import my_log
from interface_object03.sys_libs.ddt import ddt,data
from interface_object03.common.constant import DATA_DIR
from interface_object03.common.read_mysql import ReadSQL
from interface_object03.common.read_config import myconf
from interface_object03.common.read_excel import ReadExcel
from interface_object03.common.test_replace import data_replace
from interface_object03.common.http_requests import HTTPSession


data_file_path = os.path.join(DATA_DIR,'cases.xlsx')

@ddt
class WithdrawTestCase(unittest.TestCase):
    '''取现接口的测试用例类'''
    excel = ReadExcel(data_file_path,'withdraw')
    cases = excel.read_cases_obj()
    http = HTTPSession()
    db = ReadSQL()
    @data(*cases)
    def test_withdraw(self,case):
        # 第一步：准备用例数据
        # 替换动态化的参数
        data = data_replace(case.data)
        # 获取取现之前的账户余额
        if case.check_sql:
            # 将需要格式化的字符串提取出来，替换为格式化的参数
            case.check_sql = case.check_sql.replace('#phone#', myconf.get('data', 'phone'))
            start_money = self.db.fetchone(case.check_sql)[0]
            print('提现前用户账户余额：{}'.format(start_money))

        # 第二步：读取配置文件，发送请求，将请求内容输出日志到指定目录，获取请求结果
        my_log.info("请求地址:{},请求接口{}，请求内容：{}".format(myconf.get('url','url')+case.url,case.interface,eval(data)))
        response = self.http.request(method=case.method,url=myconf.get('url','url')+case.url,data=eval(data))
        res = response.json()
        # 第三步：对比实际和预期结果
        try:
            self.assertEqual(str(case.excepted_code),res['code'])
            if case.check_sql:
                # 将需要格式化的字符串提取出来，替换为格式化的参数
                case.check_sql = case.check_sql.replace('#phone#',myconf.get('data','phone'))
                # 获取取现用例之后的余额
                end_money = self.db.fetchone(case.check_sql)[0]
                print('取现后用户账户余额：{}'.format(end_money))
                # 获取本次取现余额
                money = eval(case.data)['amount']
                # decimal.Decimal(str(money))
                # 获取数据库变化的金额
                change_money = start_money-end_money
                # 对比提现金额和数据库变化金额
                self.assertEqual(money,float(change_money))
        except AssertionError as error:
            print('测试用例不通过')
            print('预期响应状态码为:{}'.format(case.excepted_code))
            print('实际响应状态码为:{}'.format(res['code']))
            self.excel.write_data(row=case.case_id+1,column=8,value='failed')
            my_log.info('用例{}执行未通过'.format(case.title))
            my_log.exception(error)
            raise error
        else:
            print('测试用例通过')
            print('预期响应状态码为:{}'.format(case.excepted_code))
            print('实际响应状态码为:{}'.format(res['code']))
            self.excel.write_data(row=case.case_id + 1, column=8, value='passed')
            my_log.info('用例{}执行通过'.format(case.title))