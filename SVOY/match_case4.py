"""сформирован словарь, для подключения к базе данных"""

# с помощью функции connect_db(recuest), проверяем данные из словаря и если все норм,
# то возвращаем результат подключения к базе.

def connect_db(connect: dict) -> str: # (connect: dict) - указали, что connect - это наш словарь
    match connect: # тут connect - это и есть наш словарь, содержимое которого мы проверяем.
    # Нужно, что бы в словаре были ключи - server, login, password и port
    # если проверка успешна, то возвращаем строку в след.формате:
        case {'server': host, 'login':login, 'password': psw}:
            port = 80 # если нужен доп.элемент, которого нет в словаре
            return f'сайт: {host}, логин: {login}, пароль: {psw}, port: {port}'
        case _:
            return 'Error connection'

recuest = {'server':'rutube.ru', 'login': 'root', 'password': 'qwerty'} # словарь

resultat = connect_db(recuest)
print(resultat)

"""Более сложный пример: информация о книгах, представлена в разных форматах"""

"""сделаем функцию, которая на выходе формирует кортеж в виде
(автор, название, год, цена). Если каких-то значений нет, вместо них будет None"""

# переданные данные (data), могут быть или словарем или кортежем или списком (tuple | list | dict)
def book_tuple(data: tuple | list | dict) -> None:
    price = None # если цены нет, то она для всех проверок будет None
    match data: # кстати, проверим, что год - целое число
        case autor, title, int(year): # проверяем на наличие этих данных, если нет цены
            pass
        case autor, title, int(year), price, *_: # если кроме нужного, есть лишнее - *_
            pass # после срабатывания шаблона, сразу переход на return
        # теперь проверяем словари, начать надо с длинного варианта
        case {'autor': autor, 'title': title, 'year': int(year), 'price': price}:
            pass
        case {'autor': autor, 'title': title, 'year': int(year)}:
            pass
        case _:
            return None
    return f'автор:{autor}, название:{title}, год:{year}, цена:{price}'

book_1 = ('Балакирев', 'Python', 2022) # кортеж
book_2 = ['Балакирев', 'Python ООП', 2022, 3432.27] # список
book_3 = {'autor': 'Балакирев', 'title': 'нейросети', 'year': 2020} # словарь
book_4 = {'autor': 'Балакирев', 'title': 'графические объекты', 'year': 2020, 'price': 5430}

result = book_tuple(book_1)
print(result)







