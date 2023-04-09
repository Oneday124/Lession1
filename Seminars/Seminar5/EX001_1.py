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
# def sum_number(n: int):
#     if (n // 10) == 0:
#         return n % 10
#     return sum_number(n//10) + n % 10
# print(sum_number(2122))

# Последовательностью Фибоначчи называется последовательность чисел a0 = 0,a1 = 1, ak = ak-1+ak-2 (k>1)
# Требуется найти N-ое чтсло Фибоначчи
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-2) + fib(n-1)
#
# print(fib(11))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на саксимальные
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные на минимальные
import random

scores = [random.randint(1, 5) for x in range(30)]
print(scores)
def changeScores(scor, ln = 0):
    if scor[ln] == 5:
        scor[ln] = 1
    ln += 1
    if len(scor) > ln:
        return changeScores(scor, ln)
    else:
        return scor

print(changeScores(scores))
