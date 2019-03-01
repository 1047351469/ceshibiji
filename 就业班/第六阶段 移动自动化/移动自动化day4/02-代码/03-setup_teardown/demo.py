def setup():
    print("setup")


def teardown():
    print("teardown")


def test_login():
    print("正在登陆1")


def test_login2():
    print("正在登陆2")


def test_login3():
    print("正在登陆3")


def login():
    print("xxxx")


# pytest 会自动搜索  test开头的函数
# collected n items 表示检索到了n个测试脚本
# 格式输出不太爽，正常！
# 只有test开头才叫测试脚本
# setup和teardown会在测试脚本的一前一后执行