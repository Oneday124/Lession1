# Множества содержат в себе уникальные элементы, не обязательно упорядоченные
# Одно множество может содержать значения любых типов
# Если у вас есть 2 множества, то вы можете совершать над ними любые стандартные операции, например
# объединение, переечение, разность
"""
colors = {'red', 'green', 'blue'}
print(colors)           # {'blue', 'green', 'red'}
colors.add('red')
print(colors)           # {'red', 'blue', 'green'} Функция добавляет элемент, но если не уникальный, то не добавляет
colors.add('gray')
print(colors)           # {'blue', 'red', 'green', 'gray'}
colors.remove('red')    # {'gray', 'blue', 'green'} Удаление элемента из множества. Если элемент не найден будет ошибка
print(colors)
colors.discard('red')   # {'gray', 'blue', 'green'} Проверит если ли элемент и удалит если найдет. Ошибки не будет
print(colors)
colors.clear()          # set() Удаляет все элементы из множества
print(colors)

q = set()               # Создание множества
"""
# Операции со множествами

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
print(c)                # {1, 2, 3, 5, 8} - копирование множества

u = a.union(b)
print(u)                # {1, 2, 3, 5, 8, 13, 21} - объединение множеств

i = a.intersection(b)
print(i)                # {8, 2, 5} - пересечение

dl = a.difference(b)
print(dl)               # {1, 3} - разница a - b

dr = b.difference(a)
print(dr)               # {13, 21} - разница b - a

q = a.union(b).difference(a.intersection(b))    # ищет пересечение a и b, объединяет a и b,
                                                # из полученного мн-ва находим разность с множеством a.intersection(b)
print(q)                # {1, 21, 3, 13}

# Замороженное множество - нельзя поменять

a = {1, 8, 6}
b = frozenset(a)
print(b)                # frozenset({8, 1, 6})
