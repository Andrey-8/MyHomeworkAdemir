class Figure:

    # @property - встроенная функция, которая позволяет создавать управляемые атрибуты
    # в классах. По сути, нужно только при использовании инкапсулированных атрибутов
    # изначально количество сторон (sides_count) = 0 (атрибут или свойство класса)
    @property
    def sides_count(self):  # это не просто общее значение, а атрибутт класса,
        return 0  # потому sides_count не просто = 0 , а возвращает 0

    # сколько всего будет сторон неизвестно, потому пишем *sides)
    def __init__(self, color, *sides):
        self.__sides = list(sides)  # список сторон (целые числа)
        self.__color = list(color)  # список цветов в формате RGB
        self.filled = False  # закрашенный, bool ваще для чего эти данные

    # возвращает список RGB цветов
    def get_color(self):  # учитывая, что функцию пишем через "get_", не ясно, зачем нужен декроратор @property
        return self.__color

    # @staticmethod проверяет корректность переданных значений перед установкой нового цвета.
    # целые числа в диапазоне от 0 до 255 (включительно),  не уверен, что правильно использовал проверку
    # isinstance, нужно пояснение
    # Функция all принимает любой итерабельный объект: список, кортеж, множество, словарь или диапазон.
    # Она возвращает True, если все элементы итерируемого объекта равны True, а в противном случае — False.
    # Также функция возвращает True, если итерабельный объект пуст
    @staticmethod
    def __is_valid_color(r, g, b):
        if isinstance(Figure.sides_count, int):
            return all(0 <= x <= 255 for x in (r, g, b))

    # принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно
    # проверив их на корректность.Если введены некорректные данные, то цвет остаётся прежним.
    # не забываем, что RGB должны быть в виде списка и метод только принимает и не возвращает
    # set_ - это метод setter - присваивание значения
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    #  принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные
    #  числа all(isinstance(x, int) and x > 0 for x in new_sides)
    #  и кол-во новых сторон (параметр - new_sides) совпадает с текущим (len(new_sides) == self.sides_count),
    #  False - во всех остальных случаях
    def __is_valid_sides(self, *new_sides):
        return all(isinstance(x, int) and x > 0 for x in new_sides) and len(new_sides) == self.sides_count

    # Метод set_sides(self, *new_sides) должен принимать новые стороны. Если их количество
    # не равно sides_count, то не изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # Метод get_sides (получение сторон) должен возвращать значение я атрибута __sides (стороны)
    def get_sides(self):
        return self.__sides

    # Метод __len__ должен возвращать периметр фигуры (сумма сторон).
    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):  # наследует от базового класса
    sides_count = 1

    # круг должен обладать атрибутами длина окружности, цвет и площадь
    def __init__(self, color, length):
        super().__init__(color, length)
        self.__radius = length / (2 * 3.14)

    # возвращает площадь круга пи * r**2
    def get_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    # Метод get_square возвращает площадь треугольника
    def get_square(self):
        # получаем полупериметр (p) треугольника (сумма длины сторон) / 2
        p = sum(self.get_sides()) / 2
        # возвращаем площадь треугольника - кв.корень из p*(p - длина 1 стороны)*(p - длина 2 стороны)*(p - длина 3 стороны)
        return (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) // 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edges):
        sides = [edges] * self.sides_count
        super().__init__(color, *sides)

    # Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    def get_volume(self):
        edge = self.get_sides()[0]  # get_sides возвращает значение стороны
        return edge ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
