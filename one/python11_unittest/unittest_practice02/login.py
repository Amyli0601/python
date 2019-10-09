"""
===============
author:Administrator
time:11:48
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
    if 6<= len(password) <=18 and 6<= len(username) <=18:
        if username == 'Amy00001' and password=='123456a':
            return {"code":200,"msg":"登录成功"}
        else:
            return {"code":999,"msg":"证号或密码不正确"}
    else:
        return {"code":999,"msg":"密码长度在6-18位之间"}
