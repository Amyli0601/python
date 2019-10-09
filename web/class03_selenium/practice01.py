"""
===============
author:Administrator
time:9:53
E-mail:1223607348@qq.com
===============
"""
'''
selenium原理
selenium元素定位
'''
import time
from selenium import webdriver
# 初始化浏览器
driver = webdriver.Chrome()
print(driver)
# 访问测试网站
url = 'https://www.baidu.com'
driver.get(url)
time.sleep(2)
# # 获取网页地址
# print(driver.current_url)
# # 获取网页的标题
# print(driver.title)
# # 获取网页的源代码
# print(driver.page_source)
# 元素定位
elem = driver.find_element_by_id('kw')
print(elem.text)

# 手工测试用什么方法，selenium会有对应的方法
# 最大化
driver.maximize_window()
# 最小化
driver.minimize_window()
# 设置窗口的大小
driver.set_window_size(800,600)
# 刷新
driver.refresh()
# 后退
driver.back()
# 前进
driver.forward()
# 判断有没有对应的字符串
driver.page_source.find('柠檬班')
# 关闭浏览器、关闭服务
driver.quit()
