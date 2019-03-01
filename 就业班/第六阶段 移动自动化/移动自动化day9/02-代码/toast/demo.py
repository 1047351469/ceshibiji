from appium import webdriver
import time

# server 启动参数
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = dict()
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.164.101:5555'
# app信息
desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
desired_caps['appActivity'] = '.activities.NavigationActivity'
# 中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# toast
desired_caps['automationName'] = 'Uiautomator2'

# 声明对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def find_toast(message):
    # message = "//*[contains(@text,'" + message + "')]"

    # ele = driver.find_element(By.XPATH, "//*[contains(@text,'" + message + "')])")
    ele = WebDriverWait(driver, 5, 0.1).until(lambda x: x.find_element(By.XPATH, "//*[contains(@text,'" + message + "')]"))
    return ele.text

time.sleep(5)
driver.press_keycode(4)  # 返回
# driver.keyevent(4) # Uiautomator1
print(find_toast("退出"))