# def function_name(x):
    # body line 1
        # ...
    # body line n
    # optional return

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
# a = sum_numbers(5)
# print(a)

# Функция с неограниченным количеством аргументов
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res +=i
#     return res
#
# print(sum_str('q','e','i'))
# print(sum_str('1', '8', '9'))

# Модульность

import modul1
print(modul1.max1(5, 9))

from modul1 import max1
print(max1(10, 9))

from modul1 import *       # импорт всех функций из файла
print(max1(10, 51))