

import pytest as pytest
from appium import webdriver
import pytest

class TestLogin:

    def setup(self):
        print("前置代码_setup")

    @pytest.fixture(params=[1, 2, 3])
    def data(self, request):
        print("fixture")
        return request.param

    def test_login1(self, data):
        print("test_login1")
        assert data % 3 == 0

    # def test_login2(self):
    #     print("test_login2")
    #
    # def test_login3(self):
    #     print("test_login3")