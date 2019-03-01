from time import sleep
from selenium import webdriver
# 定义获取所有窗口句柄函数
all_handle={} #定义空字典，存储所有窗口title和handle
def get_windows(windows):
    for wind in windows:
        driver.switch_to.window(wind)
        # 获取单前页面title
        title=driver.title
        # 把获取的title以键名的方式存储字典，wind以值的形式存储
        all_handle[title]=wind
    return all_handle
driver=webdriver.Firefox()
#获取当前窗口句柄
cur_window=driver.current_window_handle
driver.get(r"e:\课堂\WebDriver\注册实例.html")
driver.find_element_by_link_text("注册A网页").click()
driver.find_element_by_link_text("注册B网页").click()
# 获取所有窗口句柄
windows=driver.window_handles
# 切换指定窗口句柄
driver.switch_to.window(get_windows(windows)["注册B"])
driver.find_element_by_css_selector("#userB").send_keys("admin")
driver.find_element_by_css_selector("#passwordB").send_keys("admin")
driver.find_element_by_css_selector("#telB").send_keys("18611111111")
driver.find_element_by_css_selector("#emailB").send_keys("123-B@126.com")
sleep(3)
driver.quit()
