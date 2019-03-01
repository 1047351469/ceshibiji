# 导包
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
# 获取当前窗口句柄
current=driver.current_window_handle
print("启动后当前窗口句柄为：",current)
# 第一步定位注册A页面并点击
driver.find_element_by_partial_link_text("注册A网页").click()
# 获取所有窗口句柄
handles=driver.window_handles
print("所有窗口句柄为：",handles)
# 遍历及切换
for handle in handles:
    if handle != current:
        # 执行切换窗口方法
        driver.switch_to.window(handle)
        # 第二步填写注册A信息
        driver.find_element_by_css_selector("#userA").send_keys("admin")
        driver.find_element_by_css_selector("#passwordA").send_keys("admin")
        driver.find_element_by_css_selector("#telA").send_keys("1861111111")
        driver.find_element_by_css_selector("#emailA").send_keys("admin@123.com")
sleep(2)
driver.quit()