class Sjx():
    def sjx(self,a,b,c):
        # 判断是否为三角形
        if a+b>c and a+c>b and b+c>a:
            # 判断是否为等边三角形
            if a==b and b==c:
                return "等边三角形"
            elif a==b or a==c or b==c:
                return "等腰三角形"
            else:
                return "普通三角形"
        else:
            return "不是三角形"
if __name__ == '__main__':
    print(Sjx().sjx(2,3,4))