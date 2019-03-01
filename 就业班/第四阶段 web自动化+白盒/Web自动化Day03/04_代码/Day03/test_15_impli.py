# 导包
from time import sleep
from selenium import webdriver
# 实例化浏览器
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
# 设置隐式等待
driver.implicitly_wait(10)
sleep(2)
driver.find_element_by_css_selector("#user").send_keys("admin")
text=driver.find_element_by_css_selector("#user").get_attribute("value")
print("获取的文本值为：",text)


sleep(2)
driver.quit()