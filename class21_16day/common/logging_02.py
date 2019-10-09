"""
============================
Author:柠檬班-木森
Time:2019/8/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import logging
# 创建日志收集器
mylog = logging.getLogger('mylog')

# 设置日志收集器，收集的日志等级
mylog.setLevel('DEBUG')

# 日志输出渠道
# 创建一个日志输出渠道：输出到控制台
sh = logging.StreamHandler()
sh.setLevel('DEBUG')
# 将日志输出渠道添加到日志收集器中
mylog.addHandler(sh)



# 日志输出
# mylog.debug('---这个是debug等级的日志,一般用于调试')
# mylog.info('---这个是info等级的日志，常规信息的输出')
# mylog.warning('---这个是warning等级的日志，警告信息')
# mylog.error('---这个是error等级的日志，错误信息')
# mylog.critical('---这个是critical等级的日志，严重的错误，程序要崩溃')



def func(name):
    print(name,type(name))
    mylog.debug('name的值{}，name的类型{}'.format(name,type(name)))



print('-------1-----')
func('999')
mylog.info('函数已经指向完毕，没有出现异常信息')
print('-------2-----')

# print(aa)
#  关于warning等级的使用场景

# import openpyxl
# wb = openpyxl.load_workbook(r'C:\project\python21\class21_16day\zy_15day\cases.xlsx')
# # sh = wb['Sheet1']
# wb.get_sheet_by_name('Sheet1')