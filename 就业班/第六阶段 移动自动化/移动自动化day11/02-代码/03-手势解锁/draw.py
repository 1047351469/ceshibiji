from appium import webdriver
import time

# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.ChooseLockPattern'
# 解决输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
# # 需要进入的页面
# page_name = "安全"
#
# # 如果找到就点击，如果没有往下滑，再次重新找，直到找到。
# while True:
#     try:
#         driver.find_element_by_xpath("//*[contains(@text,'" + page_name + "')]").click()
#         break
#     except Exception:
#         driver.swipe(100, 2000, 100, 1500, 2000)
#         time.sleep(1)
#
# # 点击屏幕锁定方式
# driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定')]").click()
# # 点击图案
# driver.find_element_by_xpath("//*[contains(@text,'图案')]").click()

# 237 858 475

# TouchAction(driver).press(x=237, y=857).move_to(x=480, y=0).move_to(x=480, y=0).move_to(x=0, y=480).move_to(x=-480, y=0).perform()


# [HTTP] --> POST /wd/hub/session/f0eaea64-6ddf-4ae8-bbf6-30f0bd6765c8/touch/perform {"actions":[{"action":"press","options":{"x":237,"y":857}},{"action":"wait","options":{"ms":1000}},{"action":"moveTo","options":{"x":480,"y":0}},{"action":"release","options":{}}],"sessionId":"f0eaea64-6ddf-4ae8-bbf6-30f0bd6765c8"}
# [MJSONWP] Calling AppiumDriver.performTouch() with args: [[{"action":"press","options":{"x":237,"y":857}},{"action":"wait","options":{"ms":1000}},{"action":"moveTo","options":{"x":480,"y":0}},{"action":"release","options":{}}],"f0eaea64-6ddf-4ae8-bbf6-30f0bd6765c8"]
# [AndroidBootstrap] Sending command to android: {"cmd":"action","action":"swipe","params":{"startX":237,"startY":857,"endX":480,"endY":0,"steps":28}}
# [AndroidBootstrap] [BOOTSTRAP LOG] [debug] Got data from client: {"cmd":"action","action":"swipe","params":{"startX":237,"startY":857,"endX":480,"endY":0,"steps":28}}
# [AndroidBootstrap] [BOOTSTRAP LOG] [debug] Got command of type ACTION
# [AndroidBootstrap] [BOOTSTRAP LOG] [debug] Got command action: swipe
# [AndroidBootstrap] [BOOTSTRAP LOG] [debug] Display bounds: [0,0][1440,2560]
# [AndroidBootstrap] [BOOTSTRAP LOG] [debug] Display bounds: [0,0][1440,2560]
# [AndroidBootstrap] [BOOTSTRAP LOG] [debug] Swiping from [x=237.0, y=857.0] to [x=480.0, y=1280.0] with steps: 28
# [AndroidBootstrap] Received command result from bootstrap
# [AndroidBootstrap] [BOOTSTRAP LOG] [debug] Returning result: {"status":0,"value":true}
# [MJSONWP] Responding to client with driver.performTouch() result: true


# # 绝对
# TouchAction(driver)\
#     .press(x=237, y=857)\
#     .wait(1000)\
#     .move_to(x=480, y=0)\
#     .release()\
#     .perform()

# 相对
TouchAction(driver)\
    .press(x=237, y=857)\
    .move_to(x=480, y=0).wait(1000).release()\
    .perform()



