# 定位一组元素

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

# eles = driver.find_elements_by_id("com.android.settings:id/title")
# eles = driver.find_elements_by_class_name("android.widget.TextView")
eles = driver.find_elements_by_xpath("//*[contains(@text,'设置')]")

print(eles)
print(type(eles))
print(len(eles))

