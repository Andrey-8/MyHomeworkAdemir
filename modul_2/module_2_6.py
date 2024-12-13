for num in range(3, 21):
    password = f'{num}-'
    for i in range(1, num):
        for j in range(1, num):
            if j <= i:
                continue
            if num % (i + j) == 0:
                password += f' {i}{j}'

    print(password)
