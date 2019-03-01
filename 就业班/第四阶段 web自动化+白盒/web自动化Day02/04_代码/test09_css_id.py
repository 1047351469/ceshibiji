from time import sleep
from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
url="file://E:/课堂/WebDriver/注册A.html"
driver.get(url)

# 使用css定位-id
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector(".telA").send_keys("1861111111")

sleep(2)
driver.quit()