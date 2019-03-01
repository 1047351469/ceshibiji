# -*- coding: utf-8 -*-
import time
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.164.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 声明对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 手机时间
print(driver.device_time)
# 获取当前手机的分辨率
print(driver.get_window_size())
# 宽
print(driver.get_window_size()["width"])
print(type(driver.get_window_size()["width"]))

# time.sleep(1)

# # 音量加
# for i in range(3):
#     driver.keyevent(24)
#     # time.sleep(1)
#
# # 音量减
# # time.sleep(1)
# driver.keyevent(25)

# 打开通知栏
# driver.open_notifications()

# 获取当前网络
# print(driver.network_connection)

# 设置当前网络
# driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)


driver.get_screenshot_as_file("./xxx.png")