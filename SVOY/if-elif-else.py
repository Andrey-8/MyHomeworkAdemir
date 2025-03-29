"""оператор elif"""

# выбор пункта меню
# 1 - расстрел
# 2 - утопление
# 3 - повешение
# 4 - сжигание
# 5 - отравление

item = int(input('выберите пункт меню: '))

# код без elif:
if item == 1:
    print('расстрел')
else:
    if item == 2:
        print('утопление')
    else:
        if item == 3:
            print('повешение')
        else:
            if item == 4:
                print('сжигание')
            else:
                if item == 5:
                    print('отравление')
                else:
                    print('попробуй еще раз')

# # код c elif: по сути работает, как else и if одновременно, но первым в коде, всегда
# обязательно стоит оператор if, а последним else.
if item == 1:
    print('расстрел')
elif item == 2:
    print('утопление')
elif item == 3:
    print('повешение')
elif item == 4:
    print('сжигание')
elif item == 5:
    print('отравление')
else:
    print('попробуй еще раз')
