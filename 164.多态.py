class Dog(object):
    def work(self):
        pass


class ArmyDog(Dog):
    def work(self):
        print('追击敌人的警犬')


class DurgDog(Dog):
    def work(self):
        print('追查毒品的警犬')


class Person(object):
    def work_with_dog(self, dog):
        dog.work()


ad = ArmyDog()
dd = DurgDog()
xiaoming = Person()
xiaoming.work_with_dog(ad)
xiaoming.work_with_dog(dd)
