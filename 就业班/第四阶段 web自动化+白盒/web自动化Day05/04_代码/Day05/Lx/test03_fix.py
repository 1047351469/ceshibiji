import unittest
class Test01(unittest.TestCase):
    # 初始化首先被执行
    def test001(self):
        print("test001被执行")
    def setUp(self):
        print("setUp被执行")
    def tearDown(self):
        print("tearDown被执行")
    def test002(self):
        print("test002被执行")
if __name__ == '__main__':
    unittest.main()