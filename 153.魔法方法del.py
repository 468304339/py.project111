class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __del__(self):
        print('方法已经被删除')


haier = Washer(300, 300)
