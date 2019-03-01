# 导包 unittest、三角形函数、读取xml数据类
import unittest
from UT.Day02.Code.sjx import Sjx
from UT.Day02.ReadData.read_xml import Read_Xml
# 实例化三角形
sjxClass=Sjx()
# 实例化读取xml类
readXmlClass=Read_Xml()
class Test_Xml(unittest.TestCase):
    def test001(self):
        for i in range(readXmlClass.get_len("bian")):
            # 目的测试三角形程序
            result=sjxClass.sjx(int(readXmlClass.readXml("bian",i,"b1")),
                                int(readXmlClass.readXml("bian", i, "b2")),
                                int(readXmlClass.readXml("bian", i, "b3")))
            # 添加断言，判断三角形程序返回的结果是否符合我们预期结果
            self.assertEqual(result,readXmlClass.readXml("bian", i, "expect"))
            print(readXmlClass.readXml("bian",i,"b1"),
                  readXmlClass.readXml("bian", i, "b2"),
                  readXmlClass.readXml("bian", i, "b3"),
                  readXmlClass.readXml("bian", i, "expect"),"--》验证通过")