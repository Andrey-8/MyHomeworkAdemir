while True:

    x = int(input("введи число: "))
    count = 0
    y = 1

    if x == 0:
        break

    while count < x:
        count += 1
        y *= count
    else:
        print(f"факториал {x} = {y}, 0 - выход из цикла")
