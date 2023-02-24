try:
    f = open('test100.txt', 'r')
except Exception as e:
    f = open('test100.txt', 'w')
else:
    print('上述操作没有异常')
finally:
    f.close()
