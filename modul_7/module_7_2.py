# file_name - ФАЙЛ СО СПИСКОМ ИЗ СТРОК В ФОРМАТЕ СЛОВАРЯ, ГДЕ КЛЮЧ - КОРТЕЖ,\
#          А ЗНАЧЕНИЕ - СТРОКА
# strings - НЕПОСРЕДСТВЕННО СТРОКИ В ФАЙЛЕ

def custom_write(file_name, strings):
    strings_positions = {}  # ПОЗИЦИЯ КУРСОРА В СТРОКЕ
    strings_number = 1  # НАЧАТЬ С ПЕРВОЙ СТРОКИ
    file = open(file_name, 'w', encoding='utf-8')  # ОТКРЫТЬ ФАЙЛ В РЕЖИМЕ ЗАПИСИ
    for string in strings:  # ПЕРЕБОР СТРОК В СПИСКЕ СТРОК
        byte = file.tell()  # НОМЕР 1-ГО БАЙТА КАЖДОЙ СТРОКИ
        file.write(f'{string}\n')  # ЗАПИСАТЬ В ФАЙЛ ДАННУЮ СТРОКУ
        strings_positions[(strings_number, byte)] = string  # ВЫВОД СТРОКИ ПО ПОЗИЦИИ КУРСОРА
        strings_number += 1  # ПРИСВОЕНИЕ НОМЕРА СЛЕДУЮЩЕЙ СТРОКЕ (2, 3, 4)
    file.close()  # ЗАКРЫТИЕ ФАЙЛА
    return strings_positions  # ВОЗВРАЩЕНИЕ КОНЕЧНОЙ ПОЗИЦИИ КУРСОРА
                              # ПРИ КАЖДОМ ЦИКЛЕ ПЕРЕБОРА


# СОДЕРЖАНИЕ ТЕКСТОВОГО ФАЙЛА (4 СТРОКИ)
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

# ССЫЛКА РЕЗУЛЬТАТА НА ФУНКЦИЮ custom_write('test.txt', info)
# ГДЕ file_name - ДАНО НАЗВАНИЕ ФАЙЛА, А strings - СОДЕРЖИМОЕ
# ТЕКСТОВОГО ФАЙЛА
result = custom_write('test.txt', info)
for elem in result.items():  # ВОЗВРАТ ЗНАЧЕНИЙ РЕЗУЛЬТАТОВ, В ВИДЕ СЛОВАРЯ,
    # С ПОМОЩЬЮ КОМАНДЫ items()
    print(elem)  # ВЫВОД ПЕРЕБОРА РЕЗУЛЬТАТОВ
