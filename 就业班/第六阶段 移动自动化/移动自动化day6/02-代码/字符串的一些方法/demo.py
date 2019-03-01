def main():
    a = "20,50,80"

    # 分割字符串
    print(a.split(","))

    # 删除尾部的字符串
    print(a.rstrip("80"))

    # 判断一个变量的类型
    # if type(a) == str:
    #     print("123")
    if isinstance(a, str):
        print("123")


if __name__ == '__main__':
    main()