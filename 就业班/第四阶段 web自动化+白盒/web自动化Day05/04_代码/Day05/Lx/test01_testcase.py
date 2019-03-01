# 导入unittest
import unittest
from Day04.test01_keys import Test01
test01=Test01()
class Test01(unittest.TestCase):
    # 必须是test开头
    def test001(self):
        print("test001被执行")
        test01.test001()
    def test002(self):
        print("test002被执行")

if __name__ == '__main__':
    unittest.main()

'''
1.不能以汉字，数字，开头
2. 不能含特殊字符 空格
3. 命名重复,关键字不要使用
'''