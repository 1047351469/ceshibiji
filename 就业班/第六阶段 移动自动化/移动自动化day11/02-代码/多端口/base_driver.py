from appium import webdriver


def init_driver(port="4723"):
    # server 启动参数
    desired_caps = dict()
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
    # 不重置应用
    desired_caps['noReset'] = True
    # toast
    # desired_caps['automationName'] = 'Uiautomator2'
    # 声明对象
    driver = webdriver.Remote('http://localhost:' + port + '/wd/hub', desired_caps)
    return driver
