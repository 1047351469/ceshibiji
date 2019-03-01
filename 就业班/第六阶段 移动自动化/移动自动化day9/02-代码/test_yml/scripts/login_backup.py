import pytest
from base.base_yml import yaml_data_with_file

def data_with_key(key):
    data = yaml_data_with_file("data")[key]
    case_data_list = list()
    for case_data in data.values():
        case_data_list.append(case_data)

    print(case_data_list)

class TestLogin:

    # # ("key_word", ["1", "2", "3"])
    # @pytest.mark.parametrize("key_word", data_with_key("test_login"))
    # def test_login(self, key_word):
    #     print("点击搜索")
    #     print(key_word)
    #     print("点击返回")
    #
    # # ("key_word", ["1", "2", "3"])
    # # (("username", "password"), [("1", "pass"), ("1", "pass"), ("1", "pass")])
    #
    # #    dict  , [{user:xxx1, pass:xxx1}, {user:xxx1, pass:xxx1}]
    #
    #
    # # [  1   ,  2,    3   ]
    # # "dict",  [ {user:xxx1, pass:xxx1},{user:xxx2, pass:xxx2}, {user:xxx3, pass:xxx3} ]
    # @pytest.mark.parametrize("args", data_with_key("test_login1"))
    # def test_login1(self, args):
    #     print("点击登录")
    #     username = args["username"]
    #     password = args["password"]
    #
    #     print(username)
    #     print(password)

    # @pytest.mark.parametrize("args", data_with_key("test_login2"))
    def test_login2(self):
        data_with_key("test_login2")



# def main():
#     data = data_with_key("test_login")
#     print(data)
#
# if __name__ == '__main__':
#     main()