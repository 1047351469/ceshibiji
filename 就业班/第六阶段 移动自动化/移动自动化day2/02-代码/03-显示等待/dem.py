from appium import webdriver

# server 启动参数
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


wdw = WebDriverWait(driver, 10, 1)
wdw.until(lambda y:y.find_element_by_xpath("//*[contains(@class,'android.widget.ImageButton')]"))

# 15 0.5 id title
# WebDriverWait(driver, 15, 0.5).until(lambda x:x.finexxxxxxxx_by_id("title"))

# ele = WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@class,'android.widget.ImageButton')]"))
# ele.click()


# lambda x:x.find_element_by_xpath(xxxx)
#
# def aaa(x):
#     return x.find_element_by_xpath("")




# back_button = driver.find_element_by_xpath("//*[contains(@class,'android.widget.ImageButton')]")
