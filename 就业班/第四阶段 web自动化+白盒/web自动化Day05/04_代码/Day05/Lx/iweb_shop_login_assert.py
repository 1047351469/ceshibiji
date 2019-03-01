# 导包
import unittest
import time
import sys
from time import sleep
from selenium import webdriver
class Iweb_Login(unittest.TestCase):
    def setUp(self):
        # 实例化浏览器
        self.driver=webdriver.Firefox()
        # 打开项目网站
        self.driver.get("http://localhost/iwebshop/")
        # 浏览器最大化
        self.driver.maximize_window()
        # 设置隐式等待
        self.driver.implicitly_wait(30)
    # 正向登陆
    def test_iweb_login(self):
        # 获取driver
        driver=self.driver
        # 点击登录按钮跳转到登录页面
        driver.find_element_by_link_text("登录").click()
        # 定位用户名及操作
        driver.find_element_by_css_selector("[alt*='邮箱']").send_keys("111111")
        # 定位密码及操作
        driver.find_element_by_css_selector('[name="password"]').send_keys("123456")
        # 点击登陆按钮
        driver.find_element_by_css_selector(".submit_login").click()
        # 获取登录后的提示信息
        text=driver.find_element_by_css_selector(".loginfo").text
        try:
            self.assertIn("admin",text)
        except AssertionError:
            # 设置时间字符串（获取运行时系统时间）
            nowtime=time.strftime("%Y_%m_%d %H_%M_%S")
            driver.get_screenshot_as_file("../Image/%s--%s.jpg"%(nowtime,sys.exc_info()[1]))
            # 抛出捕获的异常
            raise AssertionError
        # 退出
        sleep(3)
        driver.find_element_by_link_text("安全退出").click()
    def tearDown(self):
        sleep(2)
        # 关闭浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()