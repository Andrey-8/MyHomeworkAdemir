import random
from random import choice

print('проверь свою интуицию')
s = [0,1,2,4,5,3,6,7,8,9,10]
f = True
while f:
    d = int(input("введи цифру от 0 до 10: "))
    if 10 >= d >= 0:
        w = choice(s)
        print(w)
    else:
        f = False
        print("СДАЛСЯ!! КОНЕЦ ИГРЫ")
    if w == d:
        f = False
        print('КРАСАВЧЕГ УГАДАЛ!!!, конец игры')


