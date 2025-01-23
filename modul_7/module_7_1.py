# Класс Product описывает товар с атрибутами: имя, вес и категория.
class Product:
    def __init__(self, name, weight, category):
        # Инициализация объекта товара.
        self.name = name         # Название товара.
        self.weight = weight     # Вес товара.
        self.category = category  # Категория товара.

    def __str__(self):
        # Метод для строкового представления объекта.
        # Возвращает строку в формате "имя, вес, категория".
        return f'{self.name}, {self.weight}, {self.category}'


# Класс Shop представляет магазин, который может работать с файлами для хранения товаров.
class Shop:
    def __init__(self):
        # Инициализация магазина.
        # Создается приватный атрибут с именем файла для хранения списка товаров.
        self.__file_name = 'products.txt'

    def get_products(self):
        # Метод для получения списка товаров из файла.
        file = open(self.__file_name, 'r')  # Открываем файл в режиме чтения.
        products = file.read()             # Читаем содержимое файла в строку.
        file.close()                       # Закрываем файл.
        return products                    # Возвращаем строку с товарами.

    def add(self, *products):
        # Метод для добавления одного или нескольких товаров в магазин.
        current_products = self.get_products()  # Получаем текущий список товаров из файла.
        file = open(self.__file_name, 'a')      # Открываем файл в режиме добавления.
        for product in products:               # Перебираем переданные товары.
            if str(product) not in current_products:
                # Если товара нет в текущем списке, добавляем его.
                file.write(str(product) + '\n')  # Записываем товар в файл.
                current_products += str(product) + '\n'  # Обновляем текущий список товаров.
            else:
                # Если товар уже есть, выводим сообщение.
                product_name = str(product).split(', ')[0]  # Извлекаем имя товара.
                print(f'Продукт {product_name} уже есть в магазине')
        file.close()  # Закрываем файл после записи.


# Создаем объект магазина.
s1 = Shop()

# Создаем товары.
p1 = Product('Potato', 50.5, 'Vegetables')  # Картофель, 50.5 кг, категория "Овощи".
p2 = Product('Spaghetti', 3.4, 'Groceries')  # Спагетти, 3.4 кг, категория "Бакалея".
p3 = Product('Potato', 5.5, 'Vegetables')    # Картофель (другая партия), 5.5 кг.

# Вывод информации о товаре p2, используется метод __str__.
print(p2)  # Ожидаемый вывод: "Spaghetti, 3.4, Groceries"

# Добавляем товары в магазин.
s1.add(p1, p2, p3)  # p1 и p2 добавятся, p3 вызовет сообщение о дубликате.

# Выводим текущий список товаров из магазина.
print(s1.get_products())