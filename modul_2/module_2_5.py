def get_matrix(n, m, value):  # создал функцию get_matrix с параметрами (n, m, value)
    matrix = []  # пустой список таблицы внутри функции get_matrix.
    for row in range(n):  # первый(внешний) цикл for для кол-ва строк матрицы, n повторов
        matrix.append([])  # В первом цикле добавил пустой список в список таблицу
        for column in range(m):  # второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
            matrix[row].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
