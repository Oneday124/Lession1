# Дано натуральрное число n  и последовательность из n  элементов
# Требуется вывести эту последовательность в обратном порядке
# В программе запрещается объявлять массивы и оспользовать циклы (даже для ввода и вывода)

# import random
# def printN(n):
#     x = random.randint(1, 10)
#     print(f"Элемент последос=вательности: {x}")
#     if n > 1:
#         printN(n - 1)
#     print(x)
#
# n = int(input('Введите n: '))
# printN(n)

# Написать функцию факториала числа N
#
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
#
# n = int(input('Введите n: '))
# print(factorial(n))

# Написать функцию для нахождения наибольшего общего делителя 2х чисел

# x = 80
# y = 60
# def nod(x, y):
#     if x < y:
#         x, y = y, x
#     if x % y == 0:
#         return y
#     return nod(y, x % y)
# print(nod(x, y))

# найти сумму цифр числа
def sum_number(n: int):
    if (n // 10) == 0:
        return n % 10
    return sum_number(n//10) + n % 10
print(sum_number(2122))