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


time.sleep(3)
driver.press_keycode(4)


def find_toast(driver, message, timeout=3):
    """
    # message: 预期要获取的toast的部分消息
    """
    message = "//*[contains(@text,'" + message + "')]" # 使用包含的方式定位

    element = WebDriverWait(driver, timeout, 0.1).until(lambda x: x.find_element(By.XPATH, message))
    return element.text

print(find_toast(driver, "退出"))
