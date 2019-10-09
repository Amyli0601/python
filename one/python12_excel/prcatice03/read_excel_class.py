"""
===============
author:Administrator
time:17:11
E-mail:1223607348@qq.com
===============
"""
import openpyxl
# 定义一个类读取excel中的数据
class ReadExcel(object):
    def __init__(self,file_name,sheet_name):
        '''
        file_name:excel文件名
        sheet_name:sheet表头表
        '''
        self.file_name =file_name
        self.sheet_name = sheet_name
    def open(self):
        '''打开工作簿和表单'''
        # 打开文件，返回一个工作簿对象
        self.wb = openpyxl.load_workbook(self.file_name)
        # print(wb)
        # 通过工作簿选中表单对象
        self.sh = self.wb[self.sheet_name]
    def read_cases(self):
        # 打开文件和表单
        self.open()
        # 按行获取所有的表格对象，每一行放在一个列表中
        rows = list(self.sh.rows)
        # 列表推导式
        # 创建一个空列表cases，存放所有的用例数据
        cases = []
        # 获取表头
        titles1 = [row.value for row in rows[0]]
        # 遍历非表头的行,和表头打包一起打包成字典，添加到cases列表中
        for row in rows[1:]:
            data = [r.value for r in row]
            case = dict(zip(titles1,data))
            cases.append(case)
        return cases
if __name__ =='__main__':
    read_excel = ReadExcel('cases.xlsx','cases')
    cases = read_excel.read_cases()
    print(cases)