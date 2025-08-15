'''программа для заказа пиццы (собираем ингридиенты)'''

def new_order() -> bool:
    answer = input(f'будете делать новый заказ? y/n: ')
    if answer == 'y':
        return False
    elif answer == 'n':
        return True


def get_order(ingridients:list) -> list: # принимает список ингридиентов
    # и вернет список
    order = []
    for ingridient in ingridients:
        # на каждой итерации, предлагаем выбрать ингридиент из списка
        command = input(f'добавить {ingridient}?; y/n: ')
        if command == 'y': # если ответ "y", то добавляем выбранный ингридиент
            # в список выбранных игридиентов ( order = [] )
            order.append(ingridient)
    return order


def check_order(order: list) -> bool: # в эьту функцию передается список игридиентов,
# которые выбрал пользователь
    if not order: # проверка наличия ингридиентов в списке
        print("Вы ничего не заказали, попробуйте еще раз")
        return new_order() # если список пустой, то вернется результат, который
            # нам выдала функция new_order()
# если список заказов не пустой (функция new_order() выдаст True), то начинаем перебирать
# данный список
    for ingridient in order:
        print(ingridient) # выводим на экран список выбранных игридиентов
    answer = input('верный заказ? y/n: ')
    if answer == 'y':
        print('заказ принят')
        return True
    else:
        return new_order()


# основная функция main, с главным циклом программы
def main() -> None: # Non - значит функция не будет ничего возвращать
    while True:
        ingridients = ["помидоры", "колбаса", "мясо", "грибы", "огурцы"]
        order = get_order(ingridients) # запускаем функцию get_order(), сразу
        # передаем в нее наш список ингридиентов, данная функция вернет выбранный
        # пользователем список ингридиентов
        if check_order(order): # проверяем, что нам вернет функция check_order,
        # она возвращает или True или False, в зависимости от того, пустой
        # список или нет.
        # если она вернет True, то exit (выход из программы), если False, то цикл
        # запускается по новой
            exit()




main()
