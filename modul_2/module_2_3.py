my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index_el = 0

while index_el < len(my_list):
    elem = my_list[index_el]
    index_el += 1
    if elem == 0:
        continue
    elif elem < 0:
        break
    print (elem)
