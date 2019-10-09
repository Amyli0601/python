"""
===============
author:Administrator
time:10:46
E-mail:1223607348@qq.com
===============
"""
# 1、
# best_language = "PHP is the best programming language in the world! "
# print(best_language.replace

# 2、
list1 = [1,2,3,4,5,6,7]
num = int(input('请输入1-7的数字：'))
if (num in list1):
    if num==6 or num==7:
        print('今天是周末')
    else:
        print('今天是周'+str(num))
else:
    print('请输入1-7的数字')


# 3、
# list2=[1,2,3,4,5]
# list2.insert(0,0)
# list2.insert(4,66)
# list2.extend([11,22,33])
# print(list2)
# list2.sort()
# print(list2)

# 4.1
# li = [1,2,3,4,5,6,7,8,9]
# print(li[2:9:3])

# 4.2
# s = 'python java php'
# print(s[7:11])

# 4.3
# tu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# list1 = tu[1::5]
# list1.reverse()
# print(list1)
