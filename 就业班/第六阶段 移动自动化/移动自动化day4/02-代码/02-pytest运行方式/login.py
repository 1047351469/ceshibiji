import pytest


def test_login():
    print("正在登陆")

if __name__ == '__main__':
    # pytest.main("-s login.py")
    pytest.main(["-s", "login.py"])

# . 通过
# F 不通过

# pytest运行方式
# - 命令行(用的多)
# - - pytest -s xxxxx.py
# - 代码
# - - pytest.main("-s xxxxx.py")

# 如何快速打开终端并且进入当前项目目录？
# 控制台下方，有一个 terminal

# 补充：如果快读进入测试python代码的程序（类型ipython）
# 控制台下方，有一个 python console


