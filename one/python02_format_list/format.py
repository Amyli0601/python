"""
===============
author:Administrator
time:15:23
E-mail:1223607348@qq.com
===============
"""
'''
format：格式化输出
1.{}占位
2.保留小数：{:.2f}
3.百分比格式 {:.2%}

传统的格式化输出：
1.%占位
2.任意字符：%s
3.整数类型：%d
4.浮点数:%.2f
'''
str1 = '姓名:{}\n性别:{}\n年龄:{}\n存款:{:.2f}\n完成:{:.2%}'
print(str1.format('可乐','女',18,0,0.3))

# 字符串补充左边，宽度为4
str2 = 'aa{:4>4s}'
print(str2.format('bb'))

# 数字补充右边，宽度为4
str3 = 'aa:1{:2<4d}'
print(str3.format(00))

# 右对齐，宽度为5
str4 = 'aa:{:10d}'.format(0)
print(str4)

# 左对齐，宽度为5
str5 = 'aa:{:<10d}'.format(0)
print(str5)

# %占位
str6 = "姓名:%s\n性别:%s\n年龄:%.2f"%('可乐','女',18.33)
print(str6)

