def greet(name):
    name = input("input name: ")
    return f"hello {name}!" if name else None
r = greet('Andr')
print(r)
