# # print('跑跑卡丁车')
# # print('跑跑卡丁车')
# # print('一夫当关 万夫莫开')
#
# # apple = 8
# # banana = 17
# # print(apple * banana)
#
# # =156
# # i=278
# # print(h+i)
#
# # apple = input()
# # print(apple)
#
# # banana=input()
# # print(banana)
#
# import random
# import time
#
# while True:
#     print('请发红包！！！')
#     time.sleep(2)
#     print('''
#     1，姐姐发红包
#     2，弟弟发红包
#     3，哥哥发红包
#     4，妈妈发红包
#     5，爸爸发红包
#     ''')
#     person = input('请输入你要发红包的人:')
#
#     if person == '1':
#         money = random.randint(1, 1000000000)
#         print('姐姐发了%s' % money)
#
#     elif person == '2':
#         money = random.randint(1, 1000000000)
#         print('弟弟发了%s' % money)
#
#     elif person == '3':
#         money = random.randint(1, 1000000000)
#         print('哥哥发了%s' % money)
#
#     elif person == '4':
#         money = random.randint(1, 1000000000)
#         print('妈妈发了%s' % money)
#
#     elif person == '5':
#         money =random.randint(1,100000000)
#         print('爸爸发了%s' % money)
import random

while True:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = a + b
    d = int(input('%s + %s =' % (a, b)))
    if d == c:
        print('你算对了！！')
    else:
        print('你算错了')
