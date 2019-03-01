# 导包 unittest 、三角形函数程序、读取json类
import unittest
from UT.Day02.Code.sjx import Sjx
from UT.Day02.ReadData.read_json import Read_Json

# 实例化三角形
sjxClass=Sjx()
# 实例化读取JSON类
readJsonClass=Read_Json()
class Test_Json(unittest.TestCase):
    # 测试三角形
    def test001(self):
        for i in range(len(readJsonClass.readJson())):
            # 调用三角形函数
            result=sjxClass.sjx(int(readJsonClass.readJson()[i]["b1"]),
                                int(readJsonClass.readJson()[i]["b2"]),
                                int(readJsonClass.readJson()[i]["b3"]))
            # 断言 三角形返回的结果是否与预期结果相符
            self.assertEqual(result,readJsonClass.readJson()[i]["expect"])
            # 打印运行参数及结果
            print(readJsonClass.readJson()[i]["b1"],
                  readJsonClass.readJson()[i]["b2"],
                  readJsonClass.readJson()[i]["b3"],
                  readJsonClass.readJson()[i]["expect"],"--->通过！")

if __name__ == '__main__':
    unittest.main()