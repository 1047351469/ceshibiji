from time import sleep

from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
url="file://E:/课堂/WebDriver/注册A.html"
driver.get(url)

# 使用partial_link_text定位
'''
传入要定位的元素，全部文本
click():为单击方法，在我们先使用下
find_element_by_partial_link_text():为局部匹配，必须是具有代表性的局部文本
'''
driver.find_element_by_partial_link_text("访问").click()


sleep(2)
driver.quit()