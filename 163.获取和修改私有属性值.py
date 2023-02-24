class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'调用{self.kongfu}制作煎饼果子')


class School(Master):
    def __init__(self):
        self.kongfu = '[黑马果子配方]'

    def make_cake(self):
        print(f'调用{self.kongfu}制作煎饼果子')


class Practice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎果子配方]'
        self.__money = 202222

    def get_money(self):
        return self.__money

    def set_money(self):
        self.__money = 5000

    def __info__print(self):
        print('这是私有方法')

    def make_cake(self):
        self.__init__()
        print(f'调用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(Practice):
    pass


xiaoming = Tusun()
a = xiaoming.get_money()
print(a)
xiaoming.set_money()
print(xiaoming.get_money())
