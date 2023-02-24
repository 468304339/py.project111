class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


xiaoming = Dog()
a = xiaoming.get_tooth()
print(a)
