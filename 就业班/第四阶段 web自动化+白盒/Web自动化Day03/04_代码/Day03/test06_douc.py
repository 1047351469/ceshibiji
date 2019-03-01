# 导包
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")

# 给用户名传入数据：
driver.find_element_by_css_selector("#user").send_keys("admin")

sleep(3)

'''
double_click：为鼠标双击
'''
# 实例化
ActionChains(driver).double_click(driver.find_element_by_css_selector("#user")).perform()




sleep(2)
driver.quit()