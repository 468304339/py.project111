class Dog():
    tooth = 200


wangcai = Dog()
xiaohei = Dog()
Dog.tooth = '又变黑了，呵呵'
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

wangcai.tooth = '真是个黑子'
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)
