import unittest
from UT.Day02.Common.HTMLTestRunner import HTMLTestRunner
import time

if __name__ == '__main__':
    # 声明测试套件
    discover=unittest.defaultTestLoader.discover(".",pattern="test*.py")
    # 指定报告生的目录、文件名、后缀
    dir_path="../Report/"
    nowtime=time.strftime("%Y_%m_%d %H_%M_%S")
    file_name=dir_path+nowtime+"Report.html"
    # 打开报告文件流
    with open(file_name,"wb") as f:
        # 实例化HTMLTestRunner()类
        HTMLTestRunner(stream=f,title="Web自动化测试",description="操作系统：win7").run(discover)