"""ПОЯСНЕНИЕ ПО SELF"""

"""ПИТОН, во время вызова выполнения метода (функции def), через объект (экземпляр) класса (тут pt),
автоматически подставляет в сам вызов метода параметр self (по умолчанию, потому и не прописывает его).
Этот параметр self, ссылается на конкретный экземпляр класса. Например, можно сделать еще кучу экземпляров класса
и с каждым работать отдельно, благодаря параметру self.     def set_coords(self, x, y):
        self.x = x
        self.y = y
pt = Point()
pt1 = Point()

pt1.set_coords(1, 2)

pt.set_coords(3, 4) """


class Point:
    color = "red"
    circle = 2

    def set_coords(self):
        print('вызов метода (функции) "set_coords"')


# Point.set_coords() - так первый раз я вызвал выполнение метода set_coords() - БЕЗ SELF
# если прописали в функции self и создали экземпляр класса, то так
# вызвать выполнение метода можно, только прописал ссылку на экземпляр класса Point.set_coords(pt)

# сделаем ЭКЗЕМПЛЯР класса Point
pt = Point()

pt.set_coords()  # так второй раз я вызвал выполнение метода set_coords(self) - ПРОПИСАЛ SELF В МЕТОДЕ
