from people import People

class Teacher(People):

    def xxx(self):
        self.say_hello()

    # def say_hello(self):
    #     People.say_hello(self)





def main():
    t = Teacher()
    t.xxx()

if __name__ == '__main__':
    main()