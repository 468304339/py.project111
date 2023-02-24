class Washer():
    def print_info(self):
        print(f'洗衣机的宽是{self.width}')
        print(f'洗衣机的高是{self.height}')


haier = Washer()
haier.width = 500
haier.height = 500
haier.print_info()
