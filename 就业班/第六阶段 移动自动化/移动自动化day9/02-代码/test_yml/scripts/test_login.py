import pytest, os, sys

sys.path.append(os.getcwd())
from base.base_yml import yaml_data_with_file

def data_with_key(key):
    return yaml_data_with_file("login_data", key)


class TestLogin:

    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):
        print("测试登录 2 个数据")
        print(args["username"])
        print(args["password"])

    @pytest.mark.parametrize("args", data_with_key("test_sign_up"))
    def test_sign_up(self, args):
        print("测试注册 3 个数据")
        print(args["username"])
        print(args["password"])
        print(args["number"])
