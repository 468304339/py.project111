class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


class Home():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'房子的位置在{self.address},房屋的面积是{self.area},剩余面积为{self.free_area},屋子里的家具有{self.furniture}'

    def add_furniture(self, item):
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大')


bed = Furniture('双人床', 50)
sofa = Furniture('沙发', 100)
jia1 = Home('北京', 1000)
print(jia1)
jia1.add_furniture(bed)
print(jia1)
ball = Furniture('篮球场', 2000)
jia1.add_furniture(ball)
print(jia1)
