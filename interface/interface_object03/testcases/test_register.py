"""
===============
author:Administrator
time:16:50
E-mail:1223607348@qq.com
===============
"""
import os
import random
import unittest
from interface_object03.common.read_config import myconf
from interface_object03.sys_libs.ddt import ddt,data
from interface_object03.common.read_excel import ReadExcel
from interface_object03.common.constant import DATA_DIR
from interface_object03.common.http_requests import HTTPRequest
from interface_object03.common.mylog import my_log
from interface_object03.common.read_mysql import ReadSQL
from interface_object03.common.test_replace import data_replace

@ddt
class RegisterTestCase(unittest.TestCase):
    '''注册模块的测试用例类'''
    excel = ReadExcel(os.path.join(DATA_DIR,'cases.xlsx'),'register')
    cases =excel.read_cases_obj()
    http = HTTPRequest()
    db = ReadSQL()
    @data(*cases)
    def test_case_register(self,case):
        '''注册模块的用例执行逻辑'''
        # 第一步：准备测试用例数据
        # 随机生成手机号码
        phone = self.random_phone()
        # 替换动态化的参数random_phone
        re_data = case.data.replace('*random_phone*',phone)
        # 判断替换后的数据是否还有要替换的参数，如果有就调取函数，将参数替换为配置文件中的数据内容
        data = data_replace(re_data)
        # 第二步：读取配置文件，准备发送请求，将请求内容输出到日志文件，并获取响应结果
        my_log.info('请求地址{},请求接口{},请求内容:{}'.format(case.method,myconf.get('url','url')+case.url,case.interface,eval(data)))
        response = self.http.request(case.method,myconf.get('url','url')+case.url,eval(data))
        res = response.json()
        # 第三步：对比预期和实际结果
        try:
            self.assertEqual(eval(case.excepted),res)
            # 判断是否要进行sql校验
            if case.check_sql:
                # 将需要格式化的字符串提取出来，替换为格式化的参数
                case.check_sql = case.check_sql.replace('*random_phone*',phone)
                # 获取实际数据库查询结果
                db_res = self.db.find_count(case.check_sql)
                # 对比预期和实际结果
                self.assertEqual(1,db_res)
        except AssertionError as error:
            # 在测试报告中打印实际和预期结果
            print('用例测试不通过')
            print('实际结果为:{}'.format(res))
            print('预期结果为:{}'.format(case.excepted))
            # 将测试结果写入测试数据中
            self.excel.write_data(case.case_id+1,8,'failed')
            # 输出日志到日志文件
            my_log.debug('用例:{}测试不通过'.format(case.title))
            raise error
        else:
            # 在测试报告中打印实际和预期结果
            print('用例测试通过')
            print('实际结果为:{}'.format(res))
            print('预期结果为:{}'.format(case.excepted))
            # 将测试结果写入测试数据中
            self.excel.write_data(case.case_id+1,8,'passed')
            # 输出日志到日志文件
            my_log.debug('用例:{}测试通过'.format(case.title))

    def random_phone(self):
        # 随机生成手机号的类
        while True:
            phone = '13'
            for i in range(9):
                num = random.randint(1, 9)
                phone += str(num)
            # 数据库中查询手机号是否存在
            sql = "select * from member where MobilePhone='{}'".format(phone)
            if not self.db.find_count(sql):
                return phone




