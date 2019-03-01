# 新建Calc类
class Calc():
    # 新建add方法，返回a+b
    def add(self,a,b):
        return a+b
    # 新建sub方法，返回a-b
    def sub(self,a,b):
        return a-b

if __name__ == '__main__':
    print(Calc().add(10,10))
    print(Calc().sub(10,10))