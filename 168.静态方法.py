class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个静态方法')


wangcai = Dog()
wangcai.info_print()
Dog.info_print()
