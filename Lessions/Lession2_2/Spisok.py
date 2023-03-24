# Создание списков
"""
list_1 = []
list_1 = list()
print(list_1)       # []
list_1 = [1,2,3,8]
print(list_1)       # [1, 2, 3, 8]
print(*list_1)      # 1 2 3 8

for i in list_1:        # перебор списка в цикле
    print(i)

print(len(list_1))      # 4
print(list_1[0])        # 1
print(list_1[-1])       # 8

# Добавление элементов в список
list_1 = [1, 2, 3, 8]
print(list_1)           # [1, 2, 3, 8]
list_1.append(8)
print(list_1)           # [1, 2, 3, 8, 8]

# Пример заполнения списка
list_1 = []
for i in range(5):
    list_1.append(i)
    print(list_1)
"""
"""
# Функции списков
# Удаление последнего элемента
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop())     # 0 - Удаление последнего элемента и возвращает его.
print(list_1)           # [12, 7, -1, 21]

# Удаление конкретного элемента
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(2))     # -1 - Удаление i-того элемента и возвращение его.
print(list_1)            # [12, 7, 21, 0]

# Добавление элемента на нужную позицию
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))     # None - Добавление i-того элемента. (i, n)
print(list_1)            # [12, 7, 11, -1, 21, 0]
"""

# Срезы списков
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])                  # 1
print(list_1[1])                  # 2
print(list_1[-1])                 # 10
print(list_1[-5])                 # 6
print(list_1[:])                  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])                 # [1, 2]
print(list_1[len(list_1)-2:])     # [9, 10]
print(list_1[2:9])                # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])              # []
print(list_1[0:len(list_1):6])    # [1, 7]
print(list_1[::6])                # [1, 7]

