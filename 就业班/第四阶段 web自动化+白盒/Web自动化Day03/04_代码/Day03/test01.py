from time import sleep

from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")

# 实现需求
driver.find_element_by_css_selector("#user").send_keys("admin")
sleep(3)
driver.find_element_by_css_selector("#password").send_keys("123456")
sleep(3)
driver.find_element_by_css_selector(".tel").send_keys("18611111111")
sleep(3)
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")
sleep(3)
# 修改电话 先清除 使用clear()
driver.find_element_by_css_selector(".tel").clear()
driver.find_element_by_css_selector(".tel").send_keys("1860000000")

# 点击按钮
driver.find_element_by_css_selector("button").click()

sleep(3)
driver.quit()