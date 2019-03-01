# 导包
from time import sleep

from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
# 打开url
'''
第一种写法：url="E:\\课堂\\WebDriver\\注册A.html"
第二种写法：url=r"E:\课堂\WebDriver\注册A.html"
第三种写法：file:///E:/%E8%AF%BE%E5%A0%82/WebDriver/%E6%B3%A8%E5%86%8CA.html
r作用：被r修饰的字符串，字符串中的转义符不做转义使用
'''
# url=r"E:\课堂\WebDriver\注册A.html"
url="file://E:/课堂/WebDriver/注册A.html"
driver.get(url)
'''
\;反斜杠为转义字符，所以必须地两个\\

/：斜杠 5/3
\：目录结构

'''
driver.find_element_by_id("userA").send_keys("admin")

sleep(2)
# (ctrl+alt+空格)
driver.quit()