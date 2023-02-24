class SweetPatato():
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiment = []

    def cook(self, time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state = '已经烤糊了'

    def add_condiment(self, condiment):
        self.condiment.append(condiment)

    def __str__(self):
        return f'这个地瓜已经烤了{self.cook_time}分钟，地瓜此时的状态是{self.cook_state},已经添加的调料有{self.condiment}'


digua1 = SweetPatato()
print(digua1)
digua1.cook(6)
print(digua1)
digua1.cook(2)
print(digua1)
digua1.add_condiment('酱油，醋')
print(digua1)
digua1.add_condiment('食用盐')
print(digua1)
