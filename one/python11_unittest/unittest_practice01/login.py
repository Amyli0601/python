"""
===============
author:Administrator
time:10:52
E-mail:1223607348@qq.com
===============
"""

def login_check(username,password):
    '''
    登录校验的函数
    :param username:  账号
    :param password:  密码
    :return:
    '''
    if 6<= len(password) <=18:
        if username == 'python21' and password=='123456a':
            return {"code":200,"msg":"登录成功"}
        else:
            return {"code":999,"msg":"证号或密码不正确"}
    else:
        return {"code":999,"msg":"密码长度在6-18位之间"}
# excepted = {"code":200,"msg":"登录成功"}
# res = login_check('python21','123456a')
# if res == excepted:
#     print('测试用例通过')
# else:
#     print('测试用例不通过')