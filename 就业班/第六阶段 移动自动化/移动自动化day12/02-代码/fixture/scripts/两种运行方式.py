#需要使用pytest， 如果要跑这个脚本 记得改名




import pytest as pytest
from appium import webdriver
import pytest

class TestLogin:

    def setup(self):
        print("前置代码")

    @pytest.fixture()
    def data(self):
        print("准备数据")
        print("准备数据")
        print("准备数据")
        print("准备数据")
        print("准备数据")

    def test_login1(self, data):
        print("test_login1")

    @pytest.mark.usefixtures("data")
    def test_login2(self):
        print("test_login2")

    def test_login3(self):
        print("test_login3")


