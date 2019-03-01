import time
from appium import webdriver


# server 启动参数
desired_caps = dict()
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.164.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.browser'
desired_caps['appActivity'] = '.BrowserActivity'
# 中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 不重置应用
desired_caps['noReset'] = True
# toast
# desired_caps['automationName'] = 'Uiautomator2'
# 声明对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.find_element("android id")

contexts = driver.contexts
for i in contexts:
    print(i)

# 告诉appium接下来找到元素都是网页的东西
driver.switch_to.context("WEBVIEW_com.android.browser")

time.sleep(5)

input_text_view = driver.find_element_by_id("index-kw")
input_text_view.send_keys("10086")
commit_button = driver.find_element_by_id("index-bn")
commit_button.click()

time.sleep(5)

driver.switch_to.context("NATIVE_APP")
url_text_view = driver.find_element_by_id("com.android.browser:id/url")
url_text_view.send_keys("www.itcast.cn")

# driver.find_element("webview id")
#
# driver.switch_to.context("NATIVE_APP")
# driver.find_element("android id")


