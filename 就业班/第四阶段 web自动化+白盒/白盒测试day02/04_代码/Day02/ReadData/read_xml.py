# 导包 minidom
from xml.dom import minidom
class Read_Xml():
    def readXml(self,node,num,nodeChild):
        # 解析xml文档
        dom=minidom.parse("../DataPool/sjx.xml")
        # 获取文档对象
        root=dom.documentElement
        # 获取bian元素
        element=root.getElementsByTagName(node)[int(num)]
        # 获取指定bian元素 如b1
        return element.getElementsByTagName(nodeChild)[0].firstChild.data
    def get_len(self,node):
        # 解析xml文档
        dom=minidom.parse("../DataPool/sjx.xml")
        # 获取文档对象
        root=dom.documentElement
        # 获取bian元素
        return len(root.getElementsByTagName(node))
if __name__ == '__main__':
    print(Read_Xml().readXml("bian",0,"b3"))
    print(Read_Xml().get_len("bian"))