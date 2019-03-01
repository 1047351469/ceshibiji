# 导入unittest、三角形函数、csv读取参数类
import unittest
from UT.Day02.Code.sjx import Sjx
from UT.Day02.ReadData.read_csv import Read_Csv
# 实例化三角形
sjxClass=Sjx()
# 实例化读取csv工具
readCsvClass=Read_Csv()
class Test_Csv(unittest.TestCase):
    # 测试三角形函数程序
    def test001(self):
        for i in range(len(readCsvClass.readCsv())):
            result=sjxClass.sjx(int(readCsvClass.readCsv()[i][0]),
                                int(readCsvClass.readCsv()[i][1]),
                                int(readCsvClass.readCsv()[i][2]))
            # 断言：三角新运行完后返回的结果和预期结果做对比
            self.assertEqual(result,readCsvClass.readCsv()[i][3])
            print(readCsvClass.readCsv()[i][0],
                  readCsvClass.readCsv()[i][1],
                  readCsvClass.readCsv()[i][2],
                  readCsvClass.readCsv()[i][3],"---》验证通过")
if __name__ == '__main__':
    unittest.main()