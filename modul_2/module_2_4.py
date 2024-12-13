numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    for divisor in range(2, i):
        if i % divisor == 0:
            is_prime = False
            not_primes.append(i)
            break
    if is_prime == True and i != 1:
        primes.append(i)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')

# numbers - наша переменная
# primes - простые числа
# not_primes - непростые числа
# i - элементы переменной
# is_prime - переменная, со значением True или False (верно или фальш)


