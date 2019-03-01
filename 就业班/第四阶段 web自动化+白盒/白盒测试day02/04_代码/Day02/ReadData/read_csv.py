# 导包
import csv
class Read_Csv():
    def readCsv(self):
        # 打开csv
        with open("../DataPool/sjx.csv","r",encoding='utf-8') as f:
            datas=csv.reader(f)
            # 新建空列表，把单行返回的列表添加成整体的列表
            lines=[]
            for data in datas:
                # 添加数组
                lines.append(data)
            return lines
if __name__ == '__main__':
    print(Read_Csv().readCsv())