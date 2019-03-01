# 导入unittest
import unittest
# 导入用例（.py）
from Day05.Case.test02 import Test02
from Day05.Case.iwe_03 import Test03
if __name__ == '__main__':
    # 实例化 suite
    suite=unittest.TestSuite()
    # 调用 添加用例方法
    suite.addTest(Test02("test001"))
    suite.addTest(Test02("test003"))
    suite.addTest(Test03("test001"))

    runner=unittest.TextTestRunner()
    runner.run(suite)