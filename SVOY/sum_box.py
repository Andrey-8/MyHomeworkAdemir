"""Завершите функцию суммирования квадратов так, чтобы она возводила в квадрат каждое переданное ей число,
а затем суммировала результаты вместе."""


# For example, for [1, 2, 2] it should return 9 because
# 1**2+2**2+2**2=9


def square_sum(numbers):
    print(sum([num * num for num in numbers]))


square_sum([1, 2, 3, 4, 5])
