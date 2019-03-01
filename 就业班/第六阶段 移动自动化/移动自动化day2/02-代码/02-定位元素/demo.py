# 定位一个元素


from appium import webdriver

import time

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 通过id找到 放大镜按钮
ele = driver.find_element_by_id("com.android.settings:id/search")
# 进行点击
ele.click()

time.sleep(3)

# # 通过class找到返回按钮
# back_button = driver.find_element_by_class_name("android.widget.ImageButton")


# back_button = driver.find_element_by_xpath("//*[contains(@content-desc,'收起')]")
back_button = driver.find_element_by_xpath("//*[contains(@class,'android.widget.ImageButton')]")


# 点击
back_button.click()