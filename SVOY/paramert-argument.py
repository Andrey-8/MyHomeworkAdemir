# что бы не писать повторно цикл for i in spisok1-2-3:, создаем эту функцию
# и сдвигаем вправо код (цикл), что бы поместить его в тело функции
def count_list(peremennaya, count=0):
    # count = 0 можно было тут написать значение count, но решил поместить в функцию count_list
    for i in peremennaya:  # перебирать будет не сами цифры, а индексы
        count += 1  # увидим длину списка (как если использовать len() )
    return count


spisok1 = [9, 8, 7, 6]
"""ТУТ ТИПА КУЧА КАКОГО-ТО КОДА"""
spisok2 = ["a", "a", "h"]
"""ТУТ ТИПА КУЧА КАКОГО-ТО КОДА"""
spisok3 = [9, 8, 7, 5, 7]

itog = count_list(spisok1)
itog2 = count_list(spisok2)  # аргументы
itog3 = count_list(spisok3)
print(itog2)
print(itog)
print(itog3)
print(count_list("abrakadabra"))  # функция срабатывает, даже если просто
# написать строку но ссылаясь на функцию count_list
