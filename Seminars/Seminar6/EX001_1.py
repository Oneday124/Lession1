# Даны два массива чисел. Требуется вывести те элементы первого массива (в порядке в котором они идет
# в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов
# в 1 массиве, затем N чисел - элементы первого массива. Зтем число M - кол-во элем. во 2м массиве.
# Затем элементы 2ого массива
# ввод N = 7, arr [3, 1, 3, 4, 2, 4, 12]. M = 6 arr2 = [4, 15, 43, 1, 15, 1]
# вывод 3 3 2 12
#
# def inputArr(n, arr):
#     for i in range(n):
#         i = int(input('Введите элемент массива: '))
#         arr.append(i)
#     return arr
#
# n = int(input('Введите n: '))
# arr = []
# inputArr(n, arr)
# m = int(input('Введите m: '))
# arr2 = []
# inputArr(m, arr2)
#
# for i in arr:
#     if i not in arr2:
#         print(i)

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних меньше данного.
# Сначала вводится число n - кол-во эл массива. Далее записаны N чисел - элементы массива.
# Массив состоит из целых чисел
# Ввод 5, 1 2 3 4 5 вывод 0 Ввод2 5, 1 5 1 5 1 вывод 2

# def inputArr(n, arr):
#     for i in range(n):
#         i = int(input('Введите элемент массива: '))
#         arr.append(i)
#     return arr
#
# n = int(input('Введите n: '))
# arr = []
# inputArr(n, arr)
# count = 0
# for i in range(1, n-1):
#     if arr[i - 1] < arr[i] > arr[i + 1]:
#         count += 1
# print(count)

# Дан список чисел, посчитайте сколько в нем пар элементов, равных друг другу. Считается, что любые 2
# элемента, равные друг другу образуют 1 пару, которую необходимо посчитать. Выводится список чисел.
# Все числа списка вводятся в разных строках
# Ввод: 1 2 3 2 3. Вывод 2

# def Count(arr, n):
#     count = 0
#     while (n > 0):
#         for k in range(1, len(arr)):
#             if arr[0] == arr[k]:
#                 count += 1
#                 arr.pop(k)
#                 n -= 1
#                 break
#         n -= 1
#         arr.pop(0)
#     return count
#
#
# arr = [1, 2, 3, 2, 3, 3, 3]
# n = len(arr)-1
# print(Count(arr, n))

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n  равна m и наоборот.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Ввод 300, Вывод 220, 284

# def sum_of_divisors(n):
#     divisors_sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             divisors_sum += i
#     return divisors_sum
#
# k = int(input())
# for n in range(1, k):
#     m = sum_of_divisors(n)
#     if n < m <= k and sum_of_divisors(m) == n:
#         print(n, m)

# d = [1,2, [True,False], ['Москва, Уфа', [100, 101],['True',[-2, 1]]], 7.89]
# С помощью рекурсивной ф-ции get_line_list создать на его основе одномерный списокиз значений элементов списко d.
# Функция должна возвращать новый созданный одномерный список

d = [1, 2, [True,False], ['Москва, Уфа', [100, 101], ['True', [-2, 1]]], 7.89]
def get_line_list(d, a = []):
    res = []
    for i in d:
        if type(i) == list:
            res += get_line_list(i, res)
        else:
            res.append(i)
    return res

print(get_line_list(d))