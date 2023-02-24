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
        # super(School, self).__init__()
        # super(School, self).make_cake()
        super().__init__()
        super().make_cake()


class Practice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎果子配方]'

    def make_cake(self):
        self.__init__()
        print(f'调用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    def make_old_cake(self):
        # 方法一
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

        # super(Practice, self).__init__()
        # super(Practice, self).make_cake()
        super().__init__()
        super().make_cake()


xiaoming = Practice()
xiaoming.make_old_cake()
