# 导包
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
driver.find_element_by_css_selector("#user").send_keys(Keys.ENTER,"c")