import math

from fake_math import dividef

def dividem(first, second):
    rez = first / second
    if second != 0:
        return rez
    else:
        return math.inf


result1 = dividem(69, 3)
result2 = dividem(3, 0)
result3 = dividef(49, 7)
result4 = dividef(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)