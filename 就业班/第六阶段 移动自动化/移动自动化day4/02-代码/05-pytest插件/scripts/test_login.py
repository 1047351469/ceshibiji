import random

import pytest

class TestLogin:

    # @pytest.mark.run(order=1)
    # def test_login1(self):
    #     print("1")
    #     assert False


    @pytest.mark.run(order=1)
    def test_login1(self):
        num = random.randint(1,5)
        print(num)
        if num == 1:
            print("成功")
            assert True
        else:
            print("失败")
            assert False


    # @pytest.mark.run(order=2)
    # def test_login2(self):
    #     print("2")
    #     assert True
    #
    # @pytest.mark.run(order=1.5)
    # def test_login5(self):
    #     print("1.5")
    #     assert True
    #
    # @pytest.mark.run(order=0)
    # def test_login3(self):
    #     print("0")
    #     assert True
    #
    # @pytest.mark.run(order=-1)
    # def test_login4(self):
    #     print("-1")
    #     assert True
    #
    # @pytest.mark.run(order=-2)
    # def test_login6(self):
    #     print("-2")
    #     assert True
    #
    # @pytest.mark.run(order=-1.5)
    # def test_login7(self):
    #     print("-1.5")
    #     assert True
    #
    # def test_login8(self):
    #     print("没有标记")
    #     assert True


# order
# 0 > 较小的正数 > 较大的正数 > 无标记 > 较小的负数 > 较大的负数
#


