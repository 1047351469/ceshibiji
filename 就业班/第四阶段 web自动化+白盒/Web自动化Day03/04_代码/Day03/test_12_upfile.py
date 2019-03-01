# 导包
from time import sleep
from selenium import webdriver
# 实例化浏览器
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
sleep(2)

driver.find_element_by_css_selector("[name='upfile']").send_keys("E:\课堂\WebDriver\注册A.html")

sleep(2)
driver.quit()