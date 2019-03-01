from time import sleep

from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
sleep(2)
# 点击注册A网页.html
driver.find_element_by_link_text("注册A网页").click()
sleep(2)
# 演示close（）方法
# driver.close()
'''
close()与quit()区别：1. close:关闭当前主窗口
                    2.quit：关闭由webdriver启动的所有窗口

'''

# 演示quit()方法
driver.quit()