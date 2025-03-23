lst = [12, "slovo", "dva slova", 8.0, True]
lst2 = [11, "slava", "dve slavy", 8.8, False]

"""ПОИСК В СПИСКЕ"""
print("slovo" in lst)  # выход True
print("slovo" in lst2)  # выход False

""" СЛИЯНИЕ СПИСКОВ"""
print(lst + lst2)
print(lst2 + [345])

"""ДУБЛИРОВАНИЕ СПИСКОВ"""
print(["содержимое списка " * 3])
print(lst * 3)

"""УДАЛЕНИЕ ЭЛЕМЕНТОВ ИЗ СПИСКА"""
del lst[2]  # удаление идет по индексу
print(lst)
