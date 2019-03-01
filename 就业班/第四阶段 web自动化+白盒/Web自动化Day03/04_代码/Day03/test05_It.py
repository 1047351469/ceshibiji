from time import sleep

from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")

# 获取用户名文本框大小
size=driver.find_element_by_css_selector("#user").size
print("文本框大小为：",size)
# 获取文本值
text=driver.find_element_by_link_text("访问 新浪 网站").text
print("a标签链接文本值为：",text)
# 获取元素属性值
get_attribute=driver.find_element_by_link_text("访问 新浪 网站").get_attribute("href")
print("get_attribute('href')获取后的值为：",get_attribute)
print("------------------------------------")
# 获取当前页面title
title=driver.title
print("当前页面title为：",title)

# 获取当前页面url
current_url=driver.current_url
print("当前页面url为：",current_url)

print("-------------------------------------")
# 判断span元素是否显示
is_displayed=driver.find_element_by_css_selector("span").is_displayed()
print("span元素是否显示：",is_displayed)
# 判断取消按钮是否可用
is_enabled=driver.find_element_by_css_selector("#cancel").is_enabled()
print("取消按钮是否可用：",is_enabled)




# 演示quit()方法
driver.quit()