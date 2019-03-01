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
    # 逆向登陆-密码错误
    def test_iweb_login(self):
        # 获取driver
        driver=self.driver
        # 点击登录按钮跳转到登录页面
        driver.find_element_by_link_text("登录").click()
        # 定位用户名及操作
        driver.find_element_by_css_selector("[alt*='邮箱']").send_keys("admin")
        # 定位密码及操作
        driver.find_element_by_css_selector('[name="password"]').send_keys("111111")
        # 点击登陆按钮
        driver.find_element_by_css_selector(".submit_login").click()
        # 获取登录后的提示信息
        text=driver.find_element_by_css_selector(".prompt").text
        print("密码错误后的提示信息：",text)
        try:
            self.assertIn("密码不匹1配",text)
        except AssertionError:
            nowtiem=time.strftime("%Y_%m_%d %H_%M_%S")
            print("sys.exc_info()信息为：",sys.exc_info())
            driver.get_screenshot_as_file("../Image/%s--%s.jpg"%(nowtiem,sys.exc_info()[1]))

            # 抛出异常
            raise
    def tearDown(self):
        sleep(2)
        # 关闭浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()