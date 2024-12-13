immutable_var = 11, 22, 33, "Modified"
print(immutable_var)
# immutable_var[1] = 44
# ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# Главное свойство кортежа - это невозможность изменить содержимое кортежа, после создания
mutable_list = ['11', '22', '33', 'Modified']
mutable_list[0] = 1
print(mutable_list)
