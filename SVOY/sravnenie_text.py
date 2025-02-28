"""ПРОВЕСТИ АНАЛИЗ ТЕКСТА, УБРАТЬ ПОВТОРЫ СЛОВ, СРАВНИТЬ ДВА ТЕКСТА"""
from PIL.EpsImagePlugin import split

spisok01 = set()
# сначала откроем и прочтем текстовый файл
r = open('lek1.txt', encoding="utf-8")
# сначала создадим пустое множество spisok1 (строка 2)
# после чтения файла (r.read()), получили одну строку из всего текста,
# используем метод строк (.split()), он вернет список из всех слов, пробелы и знаки переноса строки пропадут.
# что бы убрать повторы слов, сконвертируем полученный список, во множество, используя фенккию set,
# теперь добавим полученное множество в переменную spisok1, функцией .update()
spisok01.update(set(r.read().split()))
r.close()
# print(spisok1)

# теперь работа со вторым текстом:
r = open('lek2.txt', encoding="utf-8")
spisok01.update(set(r.read().split()))
r.close()
# таким образом, получаем только уникальные слова и значения из двух текстов (нет повторов)
# print(spisok01)

# теперь найдем повторяющиеся слова в двух текстовых файлах:
# сначала сделаем 2 переменных, в каждой из которых, создадим множество из списков уникальных слов и значений:
r = open('lek1.txt', encoding="utf-8")
spisok2_1 = set(r.read().split())
r.close()

r = open('lek2.txt', encoding="utf-8")
spisok2_2 = set(r.read().split())
r.close()
# сначала проверим, какие слова и значения в есть обеих множествах (повторяются). метод .intersection()
sravnenue1 = spisok2_1.intersection(spisok2_2)
# print(sravnenue1)

# теперь проверим, какие значения и слова, есть в первом списке и нет во втором. метод .difference()
sravnenue2 = spisok2_1.difference(spisok2_2)
# print(sravnenue2)

# теперь проверим, какие значения и слова, есть в первом списке и нет во втором. метод .difference()
sravnenue2_1 = spisok2_2.difference(spisok2_1)
# print(sravnenue2_1)
