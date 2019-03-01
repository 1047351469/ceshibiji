# 导包
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
# 获取当前窗口句柄
current=driver.current_window_handle
# 点击
driver.find_element_by_partial_link_text("注册A网页").click()
# 获取所有窗口句柄及遍历
for handle in driver.window_handles:
    if handle!=current:
        # 切换窗口
        driver.switch_to.window(handle)
        try:
            driver.find_element_by_css_selector("#userA").send_keys("admin")
            driver.find_element_by_css_selector("#passwordA").send_keys("admin")
            driver.find_element_by_css_selector("#telA").send_keys("1861111111")
            driver.find_element_by_css_selector("#emailAa").send_keys("admin@123.com")
        except:
            # 截图保存
            driver.get_screenshot_as_file("../Image/img02.png")
sleep(2)
driver.quit()