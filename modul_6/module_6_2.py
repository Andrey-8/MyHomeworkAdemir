class Vehicle:
    # Атрибут класса
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # список допустимых цветов для окрашивания

    # объекты класса и их атрибуты
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner  # владелец транспорта. (владелец может меняться) str
        self.__model = __model  # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power #мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = __color  # название цвета. (мы не можем менять цвет автомобиля своими руками)

        # Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
        # __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):  # распечатывает результаты методов (ссылаясь на вышеперечисленные методы, через
                            # "класс"."объект"(self))
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):  # принимает аргумент new_color, сравниваем new_color со списком допустимых цветов,
                                        # если есть,
        if new_color.lower() in self.__COLOR_VARIANTS:  # то self.__color принимает новый цвет, если нет, то принт
            self.__color = new_color  # Проверка в __COLOR_VARIANTS происходит не учитывая регистр (lower)
        else:
            print(f'Нельзя поменять цвет на {new_color}')


class Sedan(Vehicle):  # Класс Sedan дочерний от класса Vehicle
    # Атрибут класса Sedan
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
