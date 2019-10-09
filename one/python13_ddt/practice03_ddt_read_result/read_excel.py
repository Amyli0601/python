"""
===============
author:Administrator
time:17:11
E-mail:1223607348@qq.com
===============
"""
import openpyxl

# 用来存放测试用例数据
class CaseData(object):
    def __init__(self,zip_obj):
        for i in list(zip_obj):
            setattr(self,i[0],i[1])
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
    def read_cases_obj(self):
        # 打开工作簿
        self.open()
        # 创建空列表用来存放用例数据
        cases = []
        # 读取文件中的数据
        rows = list(self.sh.rows)
        # 读取表头数据
        # print(rows[0])
        titles = []
        for r in rows[0]:
            titles.append(r.value)
        for row in rows[1:]:
            # 读取每一行数据
            case = []
            for j in row:
                case.append(j.value)
            zip_obj = zip(titles, case)
            # 通过CaseData这个类创建实例对象，传了参数zip_obj
            case_data = CaseData(zip_obj)
            cases.append(case_data)
        return cases
    def write_data(self,row,column,value):
        '''
        :param row: 写入的行
        :param column: 写入的列
        :param value:写入的值
        :return:
        '''
        # 打开文件
        self.open()
         # 按照传入的行和列写入值
        cell = self.sh.cell(row=row,column=column,value=value)
        # 保存
        self.wb.save(self.file_name)
if __name__ == '__main__':
    pass