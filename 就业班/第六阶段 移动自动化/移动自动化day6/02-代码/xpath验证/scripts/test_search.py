import os, sys

import pytest

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_yml import yml_data_with_file


def data_with_key(key):
    return yml_data_with_file("search_data")[key]


class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.search_page = SearchPage(self.driver)

    def test_search(self):
        # a = len(self.driver.find_elements_by_xpath("//*[contains(@text,'设')]"))
        # a = self.driver.find_element_by_xpath("//*[@text='设']")
        a = len(self.driver.find_elements_by_xpath("//*[contains(@text,'设') and @resource-id='com.android.settings:id/category_title']"))

        print(a)

        # 验证xpath
        # //*[contains(@text,'设')] 包含
        # //*[@text='设'] 精确查找
        # //*[@text='设' and contains(@text,'设')] 多个条件
        # 多个条件的时候 and 可以不加空格