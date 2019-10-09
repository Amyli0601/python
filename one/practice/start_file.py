"""
============================
author:LiuYu
time:2019/8/19
E-mail:253342381@qq.com
============================
"""
users = [{'user': 'python21', 'password': '123456'}]
# 在一个列表里放个字典，存储用户名和密码

def register(username,password1,password2):
    # 定义一个
    for user in users:
        if username == user['user']:
            return {'code': 0, 'msg': '该账户已存在'}

    else:
        if password1 != password2:
            return {'code':0,'msg':'两次密码不一致'}
        else:
            if 6<=len(username)>=6 and 6<=len(password1)<=18:
                users.append({'user':username,'password':password2})
                return {'code':1,'msg':'注册成功'}

            else:
                return {'code':0,'msg':'账号和密码必须在6-18位之间'}