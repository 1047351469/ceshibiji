from time import sleep

from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")

sleep(2)
# 浏览器最大化
driver.maximize_window()
sleep(2)
# 改变大小
driver.set_window_size(100,200)
'''
单位为像素：px
'''
sleep(2)
# 设置浏览器大小
driver.set_window_position(300,200)


sleep(3)
driver.quit()