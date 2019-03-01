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
sleep(2)
element=(By.CSS_SELECTOR,"#userA")
# 实例化WebDriverWait
wait=WebDriverWait(driver,10)
element=wait.until(EC.presence_of_element_located(element))
element.send_keys("admin")
sleep(2)
driver.quit()