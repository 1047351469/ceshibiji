from time import sleep

from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
url="file://E:/课堂/WebDriver/注册A.html"
driver.get(url)

# 使用link_text定位
'''
传入要定位的元素，全部文本
click():为单击方法，在我们先使用下
'''
driver.find_element_by_link_text("访问 新浪 网站").click()


sleep(2)
driver.quit()