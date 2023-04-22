# Вводится список целых чисел в одну строку через пробел. Необходимооставить в нем только двузначные
# числа. Реализовать программу с использованием функции filter Результат отобразить на экране в виде
# последовательности оставшихся чисел в одну строку через пробел
# input -8 11 0 -23 140 1  -> 11 -23

# string = '-8 11 0 -23 140 1'
# list1 = list(map(int, string.split()))
# list1 = list(filter(lambda x: 9 < abs(x) < 100, list1))
# print(list1)

# Решение со строками

# string = '-8 11 0 -23 140 1'
# print(*filter(lambda x: len(str(abs(int(x)))) == 2, string.split()))


# Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N,
# состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы, идущие по диагонали
# от верхнего левого угла матрицы до ее нижнего правого угла). Результат вывести в виде таблицы чисел как показано
# в примере ниже.
# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

# n = 4
# list_1 = [[int(i == j) for i in range(n)] for j in range(n)]
# print(*list_1, sep='\n')

# Решение группы:

# n = 4
# lst = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# for r in lst:
#     print(*r)

# Преобразовать набор списков
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор
#
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
#
# и потом вернуть в исходное состояние
#
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
#
# data = list(map(list, zip(users, ids, salary)))
# print(data)
# data = [[i[j] for i in data] for j in range(len(data))]
# print(data)

# Решение группы
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
#
# a, b, c = map(list, zip(users, ids, salary))
# print(a, b, c, sep='\n')
# a, b, c = map(list, zip(a, b, c))
# print(a, b, c, sep='\n')

# Решение группы № 2

# data = list(zip(users, ids, salary))
# print(data)
# data = list(zip(*zip(users, ids, salary)))
# print(data)


# Вводится строка. Требуется используя введеную строку, сформировать N = 10 пар кортежей в формате:
# (символ, порядковый индекс)
# Первый индекс имеет занчение 0. Строка может быть короче 10 символов, а может быть длинее. т.е число пар может
# быть 10 и менее. Используйте ф-ию zip и сохрание в список с именем lst

# str1 = 'Python дай мне силы пройти этот курс до конца!'
# lst = list(zip(str1, range(0, 10)))
# print(lst)

