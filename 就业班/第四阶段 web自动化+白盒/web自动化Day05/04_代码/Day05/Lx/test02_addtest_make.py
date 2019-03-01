# 导入unittest
import unittest
# 导入用例（.py）
from Day05.Case.test02 import Test02
from Day05.Case.iwe_03 import Test03
if __name__ == '__main__':
    # 实例化 suite
    suite=unittest.TestSuite()
    # 调用 添加用例方法
    suite.addTest(unittest.makeSuite(Test02))

    # 实例化TexTestRunner（）--->测试执行
    runner=unittest.TextTestRunner()
    # 调用run方法执行
    runner.run(suite)