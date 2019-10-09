"""
===============
author:Administrator
time:17:17
E-mail:1223607348@qq.com XSQ
===============
"""
import re
'''
search:整个字符串进行匹配，如果匹配到，返回一个匹配的对象
search只会匹配到符合规则的第一个
match：从字符串头部开始匹配，返回一个匹配的对象
findall：把所有符合规则的都匹配处理，返回一个列表  
var1 匹配的规则
var2 要匹配的目标字符串 


sub：替换
参数：
var1 匹配的规则
var2 替换的字符串
var3 要匹配的目标字符串
count 要替换的次数


'''
# str1 = '123python456java789python'
#
# # # 字符串的查找方法
# # res1 = str1.find('python')
# # print(res1)
#
# # 正则
# # # match 找不到返回None
# # res2 = re.match('123',str1)
# # print(res2)
#
# # search 找不到返回None
# res3 = re.search('23',str1)
# print(res3)
#
# # findall 找不到返回空列表
# res4 = re.findall('python',str1)
# print(res4)
#
# # 替换sub
# res5 = re.sub('python','lemon',str1,count=1)
# print(res5)


str1 = '12python 4566java 789python！'
# 匹配任意字符
res1 = re.findall('.',str1)
# 匹配指定字符
res2 = re.findall(r'[1p]',str1)
# 匹配数字
res3 = re.findall(r'\d',str1)
res9 = re.findall(r'\d{3}',str1)
res10 = re.findall(r'\d{3,5}',str1)
res11 = re.findall(r'\d{3,5}?',str1)
# 匹配非数字
res4 = re.findall(r'\D',str1)
# 匹配空白字符
res5 = re.findall(r'\s',str1)
# 匹配非空白字符
res6 = re.findall(r'\S',str1)
# 匹配单词字符，如a-z,A-Z,0-9，_
res7 = re.findall(r'\w',str1)
# 匹配非单词字符
res8 = re.findall(r'\W',str1)
# + 匹配一次以上，相当于{1,}
res12 = re.findall(r'\d+',str1)
res15 = re.findall(r'\d+?',str1)
# * 0次或多次，相当于{0，}
res13 = re.findall(r'\d*',str1)
res14 = re.findall(r'\d*?',str1)

# 边界:空格或？为单词的边界
str2 = 'python12 python34 python56 th124'
# 匹配以12开头
res16 = re.findall(r'^12',str2)
res17 = re.findall(r'\bpython',str2)
# print(res17)

# 分组
res18 = re.findall(r'\bpy(th)on',str2)
res19 = re.findall(r'\bpy(th)(on)',str2)
# print(res19)


phone = '17302024220'
pwd = '123456a'
s = "{'mobilephone':'#phone#','pwd':'#pwd#','regname':'LL'}"
# res = re.findall(r'#(.+?)#',s)
# print(res)
res = re.search(r'#(.+?)#',s)
rdata = res.group()
s = re.sub(rdata,phone,s)
print(s)
# print(res.group(1))



