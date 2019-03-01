from time import sleep

from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
url="file://E:/课堂/WebDriver/注册A.html"
driver.get(url)
driver.find_element_by_tag_name("input").send_keys("admin")
sleep(2)
driver.quit()