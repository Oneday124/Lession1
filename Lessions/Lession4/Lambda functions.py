def calk2(a, b):
    return a * b

def math(op, x = 15, y=5):
    print(op(x, y))

# def calk1(a,b):             # = calk1 = lambda a, b: a + b
#     return a + b

# calk1 = lambda a, b: a + b            # = math(lambda a, b: a + b, 5, 45)
# math(calk1, 5, 45)

math(lambda a, b: a + b)

# В списке хранятся числа. Нужно выбрать только четные числа и составить список пар (число: квадрат числа)
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2,4),(8,64),(38,1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]

# def funct(arr):
#     list2 = []
#     for i in data:
#         if i % 2 == 0:
#             list2.append((i, i**2))
#     return list2
#
# print(funct(data))

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]

res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
