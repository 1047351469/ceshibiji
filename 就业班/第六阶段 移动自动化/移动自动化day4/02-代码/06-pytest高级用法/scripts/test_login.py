import random

import pytest

class TestLogin:
    # XPassed 红色    X
    # 预期 失败 结果 成功
    @pytest.mark.xfail(True, reason="")
    def test_login1(self):
        print("111")
        assert True

    # XFailed 橙色     x
    # 预期 失败 结果 失败
    @pytest.mark.xfail(True, reason="")
    def test_login2(self):
        print("22")
        assert False

    # Passed 绿色     .
    # 预期 成功 结果 成功
    @pytest.mark.xfail(False, reason="")
    def test_login3(self):
        print("33")
        assert True

    # Failed 红色     F
    # 预期 成功 结果 失败
    @pytest.mark.xfail(False, reason="")
    def test_login4(self):
        print("444")
        assert False

    # @pytest.mark.skipif(True, reason="")
    # def test_login1(self):
    #     print("111")
    #     assert True
    #
    # def test_login2(self):
    #     print("2")
    #     assert True