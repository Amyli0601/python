"""
===============
author:Administrator
time:17:11
E-mail:1223607348@qq.com
===============
"""
import openpyxl

class CaseData(object):
    '''用来存放测试用例数据'''
    def __init__(self,zip_obj):
        # 变量为zip对象
        for i in list(zip_obj):
            # 通过反射机制设置属性，将表头作为属性，data作为值
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
    def read_cases_obj(self):
        # 打开工作簿
        self.open()
        # 创建空列表用来存放用例数据
        cases = []
        # 读取文件中的数据
        rows = list(self.sh.rows)
        # 读取表头数据
        print(rows[0])
        titles = []
        for r in rows[0]:
            titles.append(r.value)
        for row in rows[1:]:
            # 读取每一行数据
            case = []
            for j in row:
                case.append(j.value)
            zip_obj = zip(titles,case)
            # 通过CaseData这个类创建实例对象，传了参数zip_obj
            case_data = CaseData(zip_obj)
            cases.append(case_data)
        return cases

if __name__ =='__main__':
    read_excel = ReadExcel('cases.xlsx', 'cases')
    pass