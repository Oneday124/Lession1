# Задайте список из N элементов, заполненных числами из промежутка [-N,N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в отдельном списке, а позиции элементов в отдельном
from random import randint
# import math

n = int(input('Введите n: '))
arr1 = []
arr2 = [1, 3]
result = 1
for i in range(n):
    arr1.append(randint(-n, n))
print(arr1)

# result = math.prod(arr1) / произведение всех чисел списка
for k in arr2:
    result *= arr1[k]
print(f'result = {result}')

