calls = 0  # счётчик вызова


def count_calls():  # Должна считать вызовы остальных функций
    global calls  # Работа с глобальной переменной
    calls += 1  # счётчик +1


def string_info(string):  # Функция string_info с параметром string
    count_calls()  # счётчик +1
    return (len(string), string.lower(), string.upper())  # Возвращаем в строку длину строки + строку
    # в верхнем регистре + нижнем регистре


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for elem in list_to_search:
        if str(string) in elem.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)