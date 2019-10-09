"""
===============
author:Administrator
time:15:27
E-mail:1223607348@qq.com
===============
"""
'''
元素定位的方式去获取要操作的元素，然后才能进行点击等操作

'''
import time
from selenium import webdriver
# 初始化浏览器
driver = webdriver.Chrome()
print(driver)
# 访问测试网站
url = 'https://www.baidu.com'
driver.get(url)
# 元素定位
# 1.通过id定位元素
id = driver.find_element_by_id('kw')
# 2.通过name定位元素
name = driver.find_element_by_name('wd')
# 3.通过class_name定位元素
class_name = driver.find_element_by_class_name('s_ipt')
# 4.通过tagname
driver.find_element_by_tag_name('input')
# 5.link_text定位超链接（a标签）
driver.find_element_by_link_text('hao123')
# 6.partial_link_text 根据超链接文本内容的一部分进行元素定位
driver.find_element_by_partial_link_text('hao')
# 7.xpath
driver.find_elements_by_xpath('')
# 8.css_selector
driver.find_element_by_css_selector('')