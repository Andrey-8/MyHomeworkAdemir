"""одномерный список"""

line = [1, 7, 6, 11, 3]

"""вложенные списки"""

img = [
    [1, 7, 6, 11, 3],
    [1, 7, 6, 11, 3],
    [1, 7, 6, 11, 3],
    [1, 7, 6, 11, 3],
    [1, 7, 6, 11, 3],
]

"""или так:"""
img1 = [
    line[:],
    line[:],
    line[:],
    line[:],
    line[:],
]  # тут можно обратиться к каждому вложенному списку
# и к элементам в каждом вложенном списке

img2 = [[line] * 5]  # тут получится вложенный список, но нельзя будет обращаться
# отдельно по индексу к его элементам

img3 = [[line[:]] * 5]  # тут получится вложенный список, но нельзя будет обращаться
# отдельно по индексу к его элементам

print(img1[1])
print(img1[1][0])
