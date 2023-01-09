# Множества - содержат в себе уникальные элементы (могут быть не упорядоченными)

colors = {'red', 'green', 'blue'}

print(type(colors))             # set - множество

colors.add('gray')
print(colors)                   # {'green', 'red', 'blue', 'gray'} - добавление элемента в множество

colors.remove('red')
print(colors)                   # {'green', 'blue', 'gray'} - удаление элемента из множества. Если пытаться удалить элемент которого нет при помощи этого метода, то будет ошибка

colors.discard('green')         # {'gray', 'blue'} - удаление элемента из множества. Не вызывает ошибки если элемента такого нет
print(colors)

colors.clear()                  # set() - очищение множества
print(colors)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                    # {1, 2, 3, 5, 8} - Создание множества на основании множества (копирование)
# u = a.union(b)                  # {1, 2, 3, 5, 8, 13, 21} - объединение множеств
# i = a.intersection(b)           # {8, 2, 5} - пересечение множеств
# dl = a.difference(b)            # {1, 3} -
# dr = b.difference(a)            # {13, 21}
# print(dr)

# Изменяемые множества

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
q = a \
    .union(b) \
    .difference(a.intersection(b))
print(q)                           # {1, 21, 3, 13}

# Неизменяемые множества

s = frozenset(a)
u = s.union(b)
print(u)                           # frozenset({1, 2, 3, 5, 8, 13, 21})