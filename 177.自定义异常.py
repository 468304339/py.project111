class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'您输入的密码长度是{self.length},密码长度不能少于{self.min_len}'


def main():
    try:
        pas = input('请输入密码')
        if len(pas) < 3:
            raise ShortInputError(len(pas), 3)
    except Exception as result:
        print(result)
    else:
        print('没有异常，密码输入完成')


main()
