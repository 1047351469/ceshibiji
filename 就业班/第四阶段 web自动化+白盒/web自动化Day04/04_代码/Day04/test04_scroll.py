# 导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
# 定义js脚本
'''
window.scrollTo(0,10000)：0：为水平像素
                          10000：滚动条为向下移动10000像素
'''
js1="window.scrollTo(0,100)"
sleep(2)
# 调用执行js语句
driver.execute_script(js1)
sleep(2)
# 把滚动条垂直位置为0
js2="window.scrollTo(0,0)"
driver.execute_script(js2)
sleep(2)
driver.quit()