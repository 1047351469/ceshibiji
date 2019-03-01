# 元素操作api


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
# 解决中文不能输入的问题
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# # 找到搜索 并且点击
# search_button = driver.find_element_by_id("com.android.settings:id/search")
# search_button.click()
#
# edit_text = driver.find_element_by_id("android:id/search_src_text")
# edit_text.send_keys("你好")
#
# time.sleep(2)
#
# edit_text.clear()


# eles = driver.find_elements_by_id("com.android.settings:id/title")
# for i in eles:
#     print(i.text)


# eles = driver.find_elements_by_class_name("android.widget.TextView")
#
# for i in eles:
#     print(i.get_attribute("name"))
#
# print("------")
#
# for i in eles:
#     print(i.get_attribute("text"))
#
# print("------")
#
# for i in eles:
#     print(i.get_attribute("className"))
#
# print("------")
#
# for i in eles:
#     print(i.get_attribute("resourceId"))



search_button = driver.find_element_by_id("com.android.settings:id/search")
print(search_button.location)

