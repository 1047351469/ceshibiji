# 导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
# 点击alert按钮
driver.find_element_by_css_selector("#alert").click()
'''处理警告框'''
# 第一步获取警告框
alert=driver.switch_to.alert
# 获取警告框文本内容
text=alert.text
print("警告框文本内容为：%s"%text)
# 调用处理方法-accept同意
# alert.accept()
# 调用处理方法-dismiss 取消
alert.dismiss()
# 输入注册信息
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("123456")
driver.find_element_by_css_selector("#tel").send_keys("18611111111")
driver.find_element_by_css_selector("#email").send_keys("132@qq.com")
sleep(2)
driver.quit()