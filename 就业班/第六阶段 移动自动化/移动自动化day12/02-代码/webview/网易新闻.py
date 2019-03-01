import time
from appium import webdriver


# server 启动参数
desired_caps = dict()
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.164.101:5555'
# app信息
desired_caps['appPackage'] = 'com.netease.newsreader.activity'
desired_caps['appActivity'] = 'com.netease.nr.phone.main.MainActivity'
# 中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 不重置应用
desired_caps['noReset'] = True
# toast
# desired_caps['automationName'] = 'Uiautomator2'
# 声明对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_xpath("//*[contains(@text,'蓝色信念')]").click()

for i in driver.contexts:
    print(i)

driver.switch_to.context("WEBVIEW_com.netease.newsreader.activity")

driver.find_element_by_class_name("subscribe__btn with-active").click()

