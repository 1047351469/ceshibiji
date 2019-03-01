from appium import webdriver

import time

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0'
desired_caps['deviceName'] = '1'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# # 获取包名
# print(driver.current_package)
# # 获取当前启动名
# print(driver.current_activity)

# 打开其他应用程序
# driver.start_activity("com.android.mms", ".ui.ConversationList")

# driver.close_app()

# driver.quit()

# driver.remove_app("cn.goapk.market")

driver.install_app("/Users/Yoson/Desktop/anzhishichang.apk")

# print(driver.is_app_installed("cn.goapk.market"))

# print(driver.page_source)

# driver.background_app(5)