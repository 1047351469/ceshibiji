class People:

    def __init__(self, age, name):
        print(id(age))
        self.age = age
        self.name = name

    def say_hello(self):
        print(self.age)
        print(self.name)

def init_driver():
    return 5


def main():
    driver = init_driver()

    print(id(driver))
    p1 = People(driver, "hao")
    p1.say_hello()



    # p1 = People("18", "hao")
    # p1 = People("18", "hao")
    # print(id(p1))
    # # print(id(p2))



    # p1.say_hello()
    # p2.say_hello()



if __name__ == '__main__':
    main()