from time import sleep

from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")

sleep(2)
# 打开第二个窗口
driver.get(r"e:\课堂\WebDriver\注册A.html")
sleep(2)
# 后退
driver.back()
sleep(2)
# 前进
driver.forward()
sleep(2)
# 刷新
driver.refresh()
sleep(3)
driver.quit()