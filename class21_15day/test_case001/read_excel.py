"""
============================
Author:柠檬班-木森
Time:2019/8/20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import openpyxl


# 定义一个类专门用例读取excel中的数据

class ReadExcel(object):
    """读取excel中的用例数据"""

    def __init__(self, file_name, sheet_name):
        """
        :param file_name: excel文件名
        :param sheet_name: sheet表单名
        """
        self.file_name = file_name
        self.sheet_name = sheet_name

    def open(self):
        """打开工作薄和表单"""
        # # 打开文件，返回一个工作薄对象
        self.wb = openpyxl.load_workbook(self.file_name)
        # 通过工作薄，选择表单对象
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        """读取所有用例数据"""

        # 打开文件和表单
        self.open()
        # 按行获取所有的表格对象，每一行的内容放在一个元祖中，以列表的形式返回
        rows = list(self.sh.rows)
        # 创建一个列表cases,存放所有的用例数据
        cases = []
        # 获取表头
        titles1 = [r.value for r in rows[0]]
        # 遍历其他的数据行，和表头进行打包，转换为字典，放到cases这个列表中
        for row in rows[1:]:
            # 获取该行数据
            data = [r.value for r in row]
            # 和表头进行打包，转换为字典
            case = dict(zip(titles1, data))
            cases.append(case)
        # 将读取出来的数据进行返回
        return cases


if __name__ == '__main__':
    do_excel = ReadExcel('cases.xlsx', 'Sheet1')
    cases = do_excel.read_data()
    print(cases)
