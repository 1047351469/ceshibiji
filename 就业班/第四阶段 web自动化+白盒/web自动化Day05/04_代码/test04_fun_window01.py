from time import sleep
from selenium import webdriver
# 定义获取指定窗口句柄函数
def get_handle(cur_window,windows,titleName):
    for win in windows:
        if win !=cur_window:
            driver.switch_to.window(win)
            #获取切换后的窗口title
            title=driver.title
            # 判断获取的title是否为指定的title
            if title==titleName:
                # 返回指定title窗口的句柄
                return win
driver=webdriver.Firefox()
#获取当前窗口句柄
cur_window=driver.current_window_handle
driver.get(r"e:\课堂\WebDriver\注册实例.html")
driver.find_element_by_link_text("注册A网页").click()
driver.find_element_by_link_text("注册B网页").click()
# 获取所有窗口句柄
windows=driver.window_handles
# 切换指定窗口句柄
driver.switch_to.window(get_handle(cur_window,windows,"注册B"))
driver.find_element_by_css_selector("#userB").send_keys("admin")
driver.find_element_by_css_selector("#passwordB").send_keys("admin")
driver.find_element_by_css_selector("#telB").send_keys("18611111111")
driver.find_element_by_css_selector("#emailB").send_keys("123-B@126.com")
sleep(3)
driver.quit()
