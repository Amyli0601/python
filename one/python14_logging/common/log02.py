"""
===============
author:Administrator
time:14:26
E-mail:1223607348@qq.com
===============
"""
import logging

# 第一步：创建日志收集器
mylog = logging.getLogger('mylog')

# 第二步:设置收集日志的等级
mylog.setLevel('DEBUG')

# 第三步：日志输出渠道
# 创建日志输出渠道，输出到控制台
sh = logging.StreamHandler()
sh.setLevel('DEBUG')
# 将日志输出渠道添加到日志收集器
mylog.addHandler(sh)

# 第四步:日志输出
mylog.debug('debug等级日志，一般用于调试')
mylog.info('info等级日志，常规信息的输出')
mylog.warning('waining等级日志，程序出现警告信息')
mylog.error('error等级日志，错误信息')
mylog.critical('critical等级日志，严重错误信息')

def func(name):
    print(name)
    mylog.debug('ces')
mylog.info('函数执行完毕，没有出现异常信息')
func('999')

# 关于warning错误等级的使用场景
import openpyxl
wb = openpyxl.load_workbook(r'E:\Testsoft\python.project\one\python13_ddt\practice03_ddt_read_result\testcases.xlsx')
wb.get_sheet_by_name('cases')