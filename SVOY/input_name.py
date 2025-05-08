def greet():
    name = input("input name: ")
    return f"hello {name}!" if name else None
r = greet()
print(r)
