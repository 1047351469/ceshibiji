

import pytest as pytest
from appium import webdriver
import pytest

class TestLogin:

    def setup(self):
        print("前置代码_setup")

    def setup_class(self):
        print("前置代码_setup_class")

    @pytest.fixture(autouse=True,scope='class')
    def data(self):
        print("fixture_class")

    @pytest.fixture(autouse=True,scope='function')
    def data2(self):
        print("fixture_func")

    def test_login1(self):
        print("test_login1")

    def test_login2(self):
        print("test_login2")

    def test_login3(self):
        print("test_login3")