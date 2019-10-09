"""
============================
Author:柠檬班-木森
Time:2019/8/20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
openpyxl：
工作簿workbook:

表单sheet:


表格cell:
"""
import openpyxl

# # 打开文件，返回一个工作薄对象
wb = openpyxl.load_workbook("cases.xlsx")

# 通过工作薄，选择表单对象
sh = wb['Sheet1']

# 按行获取所有的表格对象，每一行的内容放在一个元祖中
rows = list(sh.rows)

# 创建一个列表cases,存放所有的用例数据
cases = []
# 获取表头
titles1 = [row.value for row in rows[0]]

# 遍历其他的数据行，和表头进行打包，转换为字典，放到cases这个列表中
for row in rows[1:]:
    data = [r.value for r in row]
    case = dict(zip(titles1,data))
    cases.append(case)


print(cases)

