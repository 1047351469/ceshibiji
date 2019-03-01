# 导包
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
# 设置cookie
str={"id":"userId","name":"testName"}
driver.add_cookie(str)
# 获取当前页面所有cookie
driver.get_cookie()
cookies=driver.get_cookies()
for cook in cookies:
    print("%s--->%s"%(cook["id"],cook["name"]))
print("-----------------")
driver.quit()