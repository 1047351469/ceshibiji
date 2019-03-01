# 导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
# 最上注册信息
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("admin")
driver.find_element_by_css_selector("#tel").send_keys("1861111111")
driver.find_element_by_css_selector("#email").send_keys("admin@123.com")
# 切换到注册A  frame表单
driver.switch_to.frame("myframe1")
# 左侧注册信息
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("admin")
driver.find_element_by_css_selector("#telA").send_keys("1861111111")
driver.find_element_by_css_selector("#emailA").send_keys("admin@123.com")
# 恢复到主页面 --->因为只有主页面才有frame标签
driver.switch_to.default_content()
# 切换到注册B  frame表单
driver.switch_to.frame("myframe2")
# 右侧注册信息
driver.find_element_by_css_selector("#userB").send_keys("admin")
driver.find_element_by_css_selector("#passwordB").send_keys("admin")
driver.find_element_by_css_selector("#telB").send_keys("1861111111")
driver.find_element_by_css_selector("#emailB").send_keys("admin@123.com")
sleep(2)
driver.quit()