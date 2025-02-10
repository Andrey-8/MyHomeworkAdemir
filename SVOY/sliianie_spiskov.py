# def name(onne, *args, key):
#     print(onne, args, key)
#     
# name(12, 34, 23, key = 11)

# ЗАДАЧА - создать ИЗ НЕСКОЛЬКИХ СПИСКОВ 1 СПИСОК, В КОТОРОМ НЕ БУДЕТ ОДИНАКОВЫХ ЗНАЧЕНИЙ
# И ОТСОРТИРОВАТЬ ЭТИ ЗНАЧЕНИЯ:

def excluziv_item(*args, key = False): # списки (см.ниже (per, rew, xer)), передаются в (*args) и
                           # получается кортеж из 3-х списков, который мы будем обрабатывать
                           # в цикле for
    new_list = []         # определим список new_list, как изначально пустой                       
    for i in args:
        for y in i:
            if y not in new_list:    # если значение Y нет в списке new_list
                new_list.append(y)
    if key == True:                # если значение key является True, то будем сортировать список
        new_list.sort()
    else:                            # если значение key является False, то будем сортировать список
        new_list.sort(reverse=True)   # в обратную сторону
        
    return new_list

# сделаем несколько списков, которыми будет пополнятся список new_list
per = [9, 7, 6, 5]
rew = [7, 9, 5, 6, 3, 6, 1, 7]
xer = [1, 2, 3, 4, 5, 6, 7, 8]

# вышеперечисленные списки будем передавать в переменную fuck_list
# с помощью этой переменной и вызываем функцию
fuck_list = excluziv_item(per, rew, xer, key = False)
print(fuck_list)
