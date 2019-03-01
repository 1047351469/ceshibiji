# 导包
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
sleep(2)

'''
move_to_element:鼠标悬停
'''

# 演示鼠标悬停
ActionChains(driver).move_to_element(driver.find_element_by_css_selector("button")).perform()





sleep(2)
driver.quit()