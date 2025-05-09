"""ПОПУЛЯРНЫЕ МЕТОДЫ СЛОВАРЕЙ"""
# способы создания словаря:
d1 = {'a': 7, 'b': 9}
d2 = dict([[1, 2], [3, 4], [5, 6]])
d3 = dict.fromkeys([1, 2, 3, 4, 5], 'znachenie')

d5 = d1.copy()  # копирует словарь в другую переменную
print(d1.items())  # items - возвращает словать в виде кортежей, Нужно, при использовании
# цикла for. вывод будет такой: dict_items([('a', 7), ('b', 9)]).
print(d1.keys())  # возвращает ключи словаря dict_keys(['a', 'b'])
print(d1.values())  # возвращает значения словаря dict_values([7, 9])
d1.update(d2)  # объединяет словари, заменяя значения в одинаковых ключах
print(d1)  # {'a': 7, 'b': 9, 1: 2, 3: 4, 5: 6}
print(d1.get('b'))  # возвращает значение по ключу, если такого ключа нет, то возвращает None
t = d1.pop('a')  # переносит значение в другую переменную, удаляя ключ:значение из словаря
print(d1, t)  # на выходе {'b': 9, 1: 2, 3: 4, 5: 6} 7
