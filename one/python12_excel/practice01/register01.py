"""
===============
author:Administrator
time:15:25
E-mail:1223607348@qq.com
===============
"""
users = [{'user': 'python01', 'password': '123456a'}]
def register_check(username,password1,password2):
    # 注册功能
    # 遍历出所有账号，判断账号是否存在

    # flag = False
    for user in users:
        # print(username == user['user'])
        if username == user['user']:
        # 账号存在
            # flag=True
    # if flag:
            return {"code":0,"msg":"该账户已存在"}
        else:
            if password1!= password2:
            # 两次密码不一致
                return {"code":0,"msg":"两次密码不一致"}
            else:
                # 判断账号密码长度是否在6-18位
                if 6<=len(username)<=18 and 6<=len(password2)<=18 and 6<=len(password1)<=18:
                    # 注册账号
                    users.append({'user':username,'password':password2})
                    return {"code":1,"msg":"注册成功"}
                else:
                    # 账号密码长度不对，注册失败
                    return {"code":0,"msg":"账号和密码必须在6-18位之间"}
