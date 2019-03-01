from time import sleep

from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
# 添加cookie
driver.add_cookie({'name':'BAIDUID','value':'8C5B9E84C11888F5D4BB7D0F826CD9D3:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'EVuZkl1bFE1aGNScDJMNVF-cU5HeU9GbXprV1ZIU2ZWNERPUmdaZXlTTUJSaFpiQVFBQUFBJCQAAAAAAAAAAAEAAAD82ggPMTUwNjkxNTU1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG57loBue5aS'})

# 获取单个cookie
print("get_cookie值为：",driver.get_cookie("name"))

# 获取所有的cookies
for cookie in driver.get_cookies():
    print("%s---->%s"%(cookie["name"],cookie["value"]))

sleep(3)
# 刷新
driver.refresh()
sleep(3)
driver.quit()