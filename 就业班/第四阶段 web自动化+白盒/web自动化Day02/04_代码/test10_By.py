from time import sleep
from selenium import webdriver
# 实例化浏览器
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
url="file://E:/课堂/WebDriver/注册A.html"
driver.get(url)

# 使用By类
driver.find_element(By.CSS_SELECTOR,"#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123234")
sleep(2)
driver.quit()