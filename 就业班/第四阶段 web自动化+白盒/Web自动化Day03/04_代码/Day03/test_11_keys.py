# 导包
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
# 实例化浏览器
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
sleep(2)

# 给用户名输入 admin1
driver.find_element_by_css_selector("#user").send_keys("admin1")
sleep(2)
# 删除用户名1
driver.find_element_by_css_selector("#user").send_keys(Keys.BACK_SPACE)
sleep(2)
# 全选
driver.find_element_by_css_selector("#user").send_keys(Keys.CONTROL,'a')

sleep(2)
# 复制
driver.find_element_by_css_selector("#user").send_keys(Keys.CONTROL,"c")
# 粘贴
driver.find_element_by_css_selector("#password").send_keys(Keys.CONTROL,"v")

sleep(2)
driver.quit()