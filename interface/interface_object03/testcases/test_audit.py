"""
===============
author:Administrator
time:17:37
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
from interface_object03.common.test_replace import ConText,data_replace

data_file_path = os.path.join(DATA_DIR,'cases.xlsx')

@ddt
class AuditTestCase(unittest.TestCase):
    '''加标接口的测试用例类'''
    excel = ReadExcel(data_file_path,'audit')
    cases = excel.read_cases_obj()
    http = HTTPSession()
    db = ReadSQL()
    @data(*cases)
    def test_audit(self,case):
        # 第一步：准备用例数据
        # 替换动态化的参数
        url = myconf.get('url', 'url') + case.url
        case.data = data_replace(case.data)
        # 判断是否有有*loan_id*的参数要替换
        if "*loan_id*" in case.data:
            max_id = self.db.fetchone("SELECT max(id) FROM loan")[0]
            loan_id = max_id+1
            case.data = case.data.replace("*loan_id*",str(loan_id))

        # 第二步：读取配置文件，发送请求，将请求内容输出日志到指定目录，获取请求结果
        my_log.info("请求地址:{},请求接口{}，请求内容：{}".format(url,case.interface,eval(case.data)))
        response = self.http.request(method=case.method,url=url,data=eval(case.data))
        res = response.json()

        # 判断是否在执行加标的测试用例
        if case.interface =='加标':
            loan_id =self.db.fetchone('select id from loan where MemberID = "{}" order by id desc'.format(myconf.get('data','memberId')))
            # 将添加的标id，保存为临时变量
            setattr(ConText,'loan_id',loan_id[0])
        # 第三步：对比实际和预期结果
        try:
            self.assertEqual(str(case.excepted_code),res['code'])
            if case.check_sql:
                case.check_sql = data_replace(case.check_sql)
                # 获取当前用户数据库标的状态
                status = self.db.fetchone(case.check_sql)[0]
                # 对比预期状态和实际状态
                self.assertEqual(eval(case.data)["status"],status)
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