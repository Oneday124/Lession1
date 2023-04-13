# Функция MAP принимает на вход 2 аргумента. Первый аргумент это сама функция, которую мы передаем
# Второй аргумент это объект. И наша функция применяет функцию, которую мы передаем ко всем элементам нашего
# объекта и возвращает его

# list1 = [x for x in range(1, 20)]
# print(list1)
# list1 = list(map(lambda x: x + 10, list1))
# print(list1)

# Задача: С клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел
# Этот набор чисел будет считан в качестве строки.
# Как превратить list строк в list чисел?

data = '15 156 96 3 5 8 52 5'

data = list(map(int, data.split()))
print(data)

# заменим функцию select из прошлой задачи с листа Lambda Function на функцию map (так как это одно и то же)
# def select(f, col):
#     return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]

res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)
