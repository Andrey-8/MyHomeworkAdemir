"""полиморфизм"""

# простой пример полиморфизма:
d = 'fuck ' * 8 # взаимодействие  разных типов данных
print(d) # fuck fuck fuck fuck fuck fuck fuck fuck

# к примеру, выясним площадь комнаты
class Room: # комната
    def __init__(self,l,w): # l,w - длина и ширина
        self.l = l # создаем 2 свойства l - длина и
        self.w = w # w - ширина

    # теперь напишем метод, который будет возвращать площадь комнаты
    def get_s(self):
        return self.l * self.w

    # что бы можно было просто сложить площади обеих комнат, без ссылки на метод (get_s())
    def __add__(self, other): # тут self - это room_1, a other - room_2
        # а вот тут укажем метод
        return self.get_s() + other.get_s()


room_1 = Room(3,5) # 1-я комната
room_2 = Room(4,7) # 2-я комната

print(room_1.get_s())
print(room_2.get_s())

# попытаемся просто сложить площади обеих комнат
s = room_1 + room_2
print(s)