# 导包
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
'''
ctrl+p
'''
element=driver.find_element_by_css_selector("#user")
'''
element:为元素定位位置
perform：为执行所有鼠标动作
'''
ActionChains(driver).context_click(element).perform()

sleep(2)
driver.quit()