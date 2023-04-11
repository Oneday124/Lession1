# Заполните массив элементами арифметической прогрессии. Ее первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула прогрессии an = a1 + (n-1) * d
# input 7 2 5
# output 7 9 11 13 15

# a = int(input('Введите первый элемент: '))
# n = int(input('Введите разность: '))
# d = int(input('Введите количество элементов: '))
#
# def Progression(a, n, d):
#     arr = []
#     for i in range(d):
#         an = a + n * i
#         arr.append(an)
#     return arr
#
# print(Progression(a, n, d))


# Определить индексы лементов массива (списка), значения которых принадлежат заданному диапазону (т.е не
# меньше заданного минимума и не больше заданного максимума)
# inout [-5, 9, 0, 9, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# output [1, 9, 13, 14, 19]

arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minArr = int(input('Введите минимум: '))
maxArr = int(input('Введите максимум: '))

def IndexReturn(arr, min, max):
    arrInd = []
    for i in range(len(arr)):
        if min <= arr[i] <= max:
            arrInd.append(i)
    return arrInd

print(IndexReturn(arr, minArr, maxArr))