"""учет машин на парковке, запись машин-владельцев в файл"""
from pathlib import Path


def read_or_create_file() -> dict:
    f = Path('parking.txt') # используем модуль Path, для проверки
    # создан ли файл parking.txt
    cars = {} # создаем пустой словарь
    if f.exists(): # проверка на существование файла (f), с помощью метода
# .exists(), выводит ТРУ или ФОЛС
        with open('parking.txt', 'r', encoding='utf-8') as file:
            # для чтения файла, используем метод for
            for i in file.readlines(): # метод .readline() - каждую итерацию
            # цикла, будет возвращать по одной строке из файла
                owner,car = i[:-1].split(':')
                cars.update({owner:car})

    else: # если файла еще нет, то открываем файл в режимe создания-записи
        file = open('parking.txt', 'w')
        file.close() # теперь можно закрыть файл
    return cars # возвращаем словарь



def write_file(cars:dict) -> None:
    with open('parking.txt', 'w', encoding='utf-8') as file:
        for owner,car in cars.items():
            file.write(f'{owner}: {car}\n')


def parking() -> None: # по умолчанию ничего не возвращает (None)

    cars = read_or_create_file() # функция, которая будет создавать и открывать файл
    while True:
        command = input(
            '1 - добавить\n'
            '2 - удалить\n'
            '3 - просмотр\n'
            '4 - изменить\n'
            '5 - сохранить\n'
            'введите команду:'
        )
        if command == '1': # команда добавить
            owner = input('имя владельца авто: ') # owner - хозяин авто
            if cars.get(owner): # проверка есть ли уже это имя в словаре
                print("машина этого человека уже на парковке")
                continue # возвращаемся заново к запросу команды
            car = input('введите модель машины: ')# если хозяина с таким
            # именем нет, просим ввести модель авто
            cars[owner] = car # записываем в словарь (хозяин:машина)
        elif command == '2': # команда удалить
            owner = input('имя владельца авто: ') # owner - хозяин авто
            if cars.get(owner): # проверка есть ли уже это имя в словаре
                cars.pop(owner) # если такой есть, то удаляем из словаря
                print(f'{owner} уехал со стоянки')
            else:
                print(f'имя {owner}, не ставил машину')
        elif command == '3': # команда просмотра записей
            for owner, car in cars.items(): # перебор по ключу-значению
                print(f'{owner} - {car}')
        elif command == '4': # команда изменение записи
            owner = input('имя владельца авто: ')
            if cars.get(owner): # проверка есть ли уже это имя в словаре
                car = input('введите модель машины: ')
                cars[owner] = car
            else:
                print(f'владелец {owner}, не найден')
        elif command == '5': # сохранение записей в файл
            write_file(cars) # вызываем функцию write_file, куда передаем наш словарь
            print('данные сохранены в файл')

parking()