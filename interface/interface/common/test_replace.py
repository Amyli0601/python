"""
===============
author:Administrator
time:14:39
E-mail:1223607348@qq.com
===============
"""
'''
封装一个替换数据的方法：
封装的需求：
1、替换用例中的参数
2、简化替换的流程

实现思路：
1、获取用例数据
2、判断该用例数据是否有需要替换的参数
3、对数据进行替换
'''
import re
from interface.common.read_config import myconf


def data_replace(data):
    '''动态替换用例数据'''
    while re.search(r'#(.+?)#',data):
        res =re.search(r'#(.+?)#',data)
        # 提取要替换的内容
        re_data = res.group()
        # 提取要替换的字段
        key = res.group(1)
        try:
        # 去配置文件中读取字段对应的数据内容
            value = myconf.get('data', key)
        except:
            value = getattr(ConText,key)
        # 进行替换
        data = re.sub(re_data,str(value),data)
        # # 替换
        # data = re.sub(re_data,value,data)
    return data
class ConText:
    '''用来临时保存接口直接依赖参数的类'''
    pass
if __name__ == '__main__':
    # 对象（类）、属性名、属性值：给对象设置一个属性
    setattr(ConText,'memberId',999)
    # print(ConText.memberId)
    # 获取对象的属性
    id = getattr(ConText,'memberId')
    print(id)

