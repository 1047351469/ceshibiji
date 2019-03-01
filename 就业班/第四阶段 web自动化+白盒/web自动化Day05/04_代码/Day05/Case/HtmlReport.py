import unittest,time
from Day05.Common.HTMLTestRunner import HTMLTestRunner
# 添加测试套件
discover=unittest.defaultTestLoader.discover("./",pattern="test*.py")
if __name__ == '__main__':
    # 第一步定义报告的项目文件位置
    dir_path="../Report/"
    nowtime=time.strftime("%Y_%m_%d %H_%M_%S")
    file_name=dir_path+nowtime+"Report.html"
    # 给指定报告写入数据
    with open(file_name,"wb") as f:
        # 实例化HTMLTestRunner
        HTMLTestRunner(stream=f,title="Web自动化测试",description="操作系统：Win7").run(discover)
