# 导包
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\drop.html")
sleep(2)
source=driver.find_element_by_css_selector("#div1")
ActionChains(driver).drag_and_drop_by_offset(source,500,0).perform()





sleep(2)
driver.quit()