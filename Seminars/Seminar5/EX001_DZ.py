# Напишите программу, которая на вход принимает два числа А и В, и возводит число А в целую степень В
# с помощью рекурсии
# Пример: А = 3б В = 5 -> 243 (3**5)

# def Degree(a, b):
#     if b == 0:
#         return a
#     return Degree(a, b-1) * a
#
# print(Degree(2, 3))

# Напишите рекурсивную ф-цию sum(a,b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Нельзя использовать циклы
# Пример 2 2 -> 4

# def Sum(a, b):
#     if a < b:
#         a, b = b, a
#     if b == 0:
#         return a
#     return Sum(a + 1, b-1)
#
# print(Sum(110, 28))