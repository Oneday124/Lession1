# Одна из культовых фицек python - list comprehension (генератор списка)
# list comprehension - упрощенный подход к созданию списка, который задействует цикл for,
# а так же инструкции if-else для определения того, что окажется в финальном списке

# Создaние
# list_1 = [exp for item in iterable] - exp - что добавляем, item - индекс, iterable - коллекция

list_1 = [None for item in range(5)]
print(list_1)           # [None, None, None, None, None]

list_1 = [i for i in range(1, 10)]
print(list_1)           # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Выборка по заданному условию

# list_1 = [exp for item in iterable (if conditional)]

list_1 = [i for i in range(1, 10) if i % 2 == 0]
print(list_1)           # [2, 4, 6, 8]

# Также можно умножать, делить, прибавлять, вычитать
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)           # [0, 4, 8, 12, 16]

# Создание пары каждому из чисел (кортежи)
list_1 = [(i, i*i) for i in range(10) if i % 2 == 0]
print(list_1)           # [(0, 0), (2, 4), (4, 16), (6, 36), (8, 64)]
