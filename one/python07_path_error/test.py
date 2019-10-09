"""
===============
author:Administrator
time:12:06
E-mail:1223607348@qq.com
===============
"""
# 1、新建一个包pack，在包中新建两个模块module1.py，module2.py,
#  在module1中定义一个函数（函数实现上一次石头、剪刀布游戏的功能），
# 该函数可以通过传入的参数来控制游戏次数，然后在module2中导入module1中定义的函数，并调用。
# from pack.module1 import game
# game(3)
# 2、txt读取出来的 数据保存格式为： [{'url':'....','mobilephone':'...','pwd':...'},{.........} ,{.............}] 
# with open('case.txt','r') as f:
#    cases = f.readlines()
# list1 = []
# for i in cases:
#     i = i.replace('\n','')
#     datas =i.split(',')
#     dic = {}
#     for j in datas:
#         data = j.split(':',1)
#         dic[data[0]] = data[1]
#     list1.append(dic)
# print(list1)

# 3、 上次图书管理的作业，通过文件来实现 书籍数据的永久存储。 
book = []
books=[{'id': 1, 'name': 'java', 'location': 'A区19号'},
 {'id': 2, 'name': 'python', 'location': 'A区8号'}]
try:
    def read_data():
        global books
        with open('book.txt', 'r', encoding='utf8') as f:
            books = eval(f.read())
except:
    def write_data():
        with open('book.txt', 'w', encoding='utf8') as f:
            f.write(str(books))
def print_menu():
    # 打印菜单
    print('--------------------')
    print('【1】：添加图书')
    print('【2】：删除图书')
    print('【3】：显示所有图书')
    print('【4】：退出')
print_menu()
def add_book():
    # 添加图书
    book = {
            'id': int(input('请输入图书编号：')),
            'name': input('请输入图书名称：'),
            'location': input('请输入图书位置：')
            }
    books.append(book)
    print('添加完毕，返回菜单页面')
def del_book():
    # 删除书籍
    del_name = input('请输入您要删除的图书名称：')
    sel_books=[] # 将该输入名称的图书放入该列表
    for i in range(len(books)):
        j = books[i]
        if del_name == j['name']:
            sel_books.append(j)
    print(sel_books)
    if len(sel_books) > 0:
        print('找到{}本书籍为:{}'.format(len(sel_books), del_name))
        for i in range(len(sel_books)):
            j = sel_books[i]
            print('编号：{} 书名：{} 位置：{}'.format(j.get('id'), j.get('name'),
                                         j.get('location')))
        while True:
            del_id = int(input('请输入要删除的图书编号:'))
            for i in range(len(sel_books)):
                j = sel_books[i]
                if del_id == j['id']:
                    books.remove(j)
                    print(books)
                    return
                else:
                    print('您输入的图书编号不存在，请重新输入')
                    continue
    else:
        print('您输入的图书名称不存在,请重新输入')

def all_book():
    # 显示全部图书信息
    print('当前共有{}本书籍，所有的图书信息如下：'.format(len(books)))
    for i in range(len(books)):
        j = books[i]
        print('编号：{} 书名：{} 位置：{}'.format(j.get('id'), j.get('name'),
                                         j.get('location')))
        continue
    print('查询完毕，返回菜单页面')
def main2():
    print('------欢迎进入图书管理系统-----')
    read_data()
    while True:
        option = int(input('请输入您的选项：'))
        if option == 1:
            add_book()
            continue
        elif option == 2:
            del_book()
            continue
        elif option == 3:
            all_book()
            continue
        elif option == 4:
            print('谢谢使用，程序即将关闭')
            break
        else:
            print('您的输入有误，请重新选择')
            continue
    write_data()
main2()


