import unittest
# 导入要测试的 Calc类
from UT.Day02.Code.test01_lx01 import Calc
class Test_Calc(unittest.TestCase):
    def setUp(self):
        print("setUp被执行")
    def tearDown(self):
        print("tearDown被执行")
    def test_add(self):
        result=Calc().add(10,10)
        print("test_add方法被执行")
        self.assertEqual(result,20)
    def test_sub(self):
        result=Calc().sub(10,20)
        print("test_sub方法被执行")
        self.assertEqual(result,-10)
if __name__ == '__main__':
    # main运行当前类中所有test开头的方法
    unittest.main()