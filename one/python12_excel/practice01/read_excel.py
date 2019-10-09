"""
===============
author:Administrator
time:18:01
E-mail:1223607348@qq.com
===============
"""
import openpyxl

# 定义一个类，用来读取excel中的数据
class ReadExcel(object):
    # 读取excel中的用例数据
    def __init__(self,file_name,sheet_name):
        '''

        :param file_name: 文件名称
        :param sheet_name: sheet表单名
        '''
        self.file_name = file_name
        self.sheet_name = sheet_name
    def open_file(self):
        # 打开文件，返回一个工作簿对象
        self.wb = openpyxl.load_workbook(self.file_name)
        # 通过工作簿，选择表单对象
        self.sh01 = self.wb[self.sheet_name]
    def read_file(self):
        # 打开文件和表单
        self.open_file()
        # 按行获取所有的表格对象，每行内容放在一个
        rows = list(self.sh01.rows)
        # 创建空列表存储读取数据
        cases = []
        # 获取表头:列表推导式
        titles1 = [row.value for row in rows[0]]
        # 遍历非表头的行，和表头一起打包为一个字典
        for row in rows[1:]:
            data = [r.value for r in row]
            case = dict(zip(titles1, data))
            cases.append(case)
        return cases
if __name__=='__main__':
    do_excel = ReadExcel('cases.xlsx','test01')
    cases = do_excel.read_file()
    print(cases)








