# работа со словарем
my_dict = {"Тояма": 1988, "Рыбак": 1890, "Краб": 2000}
print(my_dict)
print(my_dict.get("Рыбак"))
print(my_dict.get("Neo"))
my_dict.update({"Niger": 3421, "Hero": 5665})
zero = my_dict.pop("Краб")
print(zero)
print(my_dict)
# Работа с множеством
my_set = {1.1, 2, 2, 1, 5, 5, "joy", "leo", ("leo", "neo")}
print(my_set)
my_set.update([8, 'hi'])
my_set.remove(2)
print(my_set)
