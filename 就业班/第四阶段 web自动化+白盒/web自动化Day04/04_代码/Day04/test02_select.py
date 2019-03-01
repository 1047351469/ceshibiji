# 导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get(r"e:\课堂\WebDriver\注册实例.html")
# 城市选项-暂停2秒后选择上海A，暂停2秒后选择重庆，暂停2秒后选择广州

# 第一种方式 -使用tag_name
'''
tags=driver.find_elements_by_tag_name("option")
for tag in tags:
    if tag.get_attribute("value")=="sh":
        sleep(2)
        tag.click()
for tag in tags:
    if tag.text=="重庆":
        tag.click()

for tag in tags:
    if tag.get_attribute("value")=="gz":
        sleep(2)
        tag.click()

'''
# 第二种 使用css
'''
driver.find_element_by_css_selector("[value='sh']").click()
sleep(2)
driver.find_element_by_css_selector("[value='cq']").click()
sleep(2)
driver.find_element_by_css_selector("[value='gz']").click()

'''
# 第三种方法 通过使用Select类来定位
# 注意：Select类只能定位select标签
webelement=driver.find_element_by_css_selector("select")
'''
# 实例化Select类
select=Select(webelement)

# 通过索引来定位
select.select_by_index(1)
sleep(2)
select.select_by_index(3)
sleep(2)
select.select_by_index(2)
'''

'''通过value属性来选择'''
'''
# 实例化Select
select=Select(webelement)
# 调用value方法
select.select_by_value("sh")
sleep(2)
select.select_by_value("cq")
sleep(2)
select.select_by_value("gz")
'''

# 通过显示文本来定位
select=Select(webelement)
select.select_by_visible_text("上海")
sleep(2)
select.select_by_visible_text("重庆")
sleep(2)
select.select_by_visible_text("广州")



sleep(2)
driver.quit()