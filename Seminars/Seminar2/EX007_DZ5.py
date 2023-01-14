# Алгоритм перемешивания списка
from random import randint
arr = []
for i in range(10):
    arr.append(i)
print(arr)
for i in arr:
    index_aleatory = randint(0, len(arr) - 1)
    temp = arr[index_aleatory]
    arr[index_aleatory] = arr[i]
    arr[i] = temp
print(arr)