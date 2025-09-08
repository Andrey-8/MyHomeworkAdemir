class Animal:
    def __init__(self, name, age): # этот метод выполняется первым, при создании экземпляра класса
        self.name = name
        self.age = age

class Cat(Animal): # в скобках название класса от которого наследуется то что есть в классе Animal

# создадим метод, запуская который, кот будет мяукать
    def mau(self):
        print('мяяяяууу')

# теперь еще и собак заведем (создадим класс собак)
class Dog(Animal): # в скобках название класса от которого наследуется то что есть в классе Animal
    def __init__(self, vtoroe_name, *args,**qwargs): # добавим элемент (второе имя собаки),
        # которого нет у кота
        super().__init__(*args, **qwargs) # привязка к имеющимся атрибутам в родительском классе
        self.vtoroe_name = vtoroe_name
    def gav(self):
        print('рррр-ГАВ!!!')



# дадим имена котам, используя метод инициации класса с ссылкой на self
cat = Cat('Timofei', 14)
print(f'имя: {cat.name},\nвозраст: {cat.age}')

cat.mau() # запускаем срабатывание метода mau()
print('------------')

dog = Dog(vtoroe_name='Балбес', name='Kuvas', age=20)
print(f'имя: {dog.name}-{dog.vtoroe_name}\nвозраст: {dog.age}')
dog.gav() # запускаем срабатывание метода gav()