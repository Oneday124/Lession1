# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n
# input a a a b c a a d c d d
# Output aa_1a_2bca_3a_4dc_1d_1d_2
# Использовать ф-ию .split()

# strData = 'a a a b c a a d c d d'
# strIst = strData.split(' ')
# dictionary = dict()
#
# for i in strIst:
#     if i in dictionary:
#         print(f'{i}_{dictionary[i]}', end= ' ')
#     else:
#         print(i, end= ' ')
#     dictionary[i] = dictionary.get(i, 0) + 1

# Пользователь вводит текст. Определить сколько различных слов в тексте
# input She sells sea shells on sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output 13

# strData = "She sells sea shells on sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# strIst = strData.lower().split()
#
# setRes = set()
# for i in strIst:
#     setRes.add(i)
# print(len(setRes))

# решение группы:
# strData = "She sells sea shells on sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# print(len(set(strData.lower().split())))

# На вход подаются 2 строки текста по одному слову из перечня "камень", "ножницы", "бумага", "ящерица", "спок"
# Первая срока выбор Тимура, вторая Руслана
# Определить кто победил или ничья. Правила игры стандартные.
# a = input('Ход Тимура: ')
# b = input('Ход Руслана: ')
# dictionary = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
#               'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
#               'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
#               'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
#               'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
#               'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
#               'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
#               'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
#               'Спок-ящерица': 'Руслан'}
# key = a + '-' + b
# print(key)
# result = ''
# for item in dictionary:
#     if item == key:
#         result = dictionary[item]
# print(result)

# решение группы
# if a == b:
#     print('Победила дружба')
# else:
#     print(f"Победил {dictionary[a + '-' + b]}")

# Дана строка, состоящая из О и Р. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших решек

# strData = 'ОРРОРОРООРРРОРРРРРРР'
# count = 0
# maxCount = 0
# for i in strData:
#     if i == 'Р':
#         count += 1
#         if count > maxCount:
#             maxCount = count
#     else:
#         count = 0
# print(maxCount)

# Решение группы
# s = input()
# t = 0
# while 'Р'*(t+1) in s:
#     t += 1
# if t != 0:
#     print(t)
# else:
#     print(0)

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга оказались не такими смышлеными.
# Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и
# выиграл спор. За помощью товарищи обратились к Вам, студентам.
# import random
#
# n = 10
# max_i = -1
# for i in range(n):
#     temp = random.randint(0, 40)
#     print(temp)
#     if temp == 0:
#         break
#     else:
#         if temp > max_i:
#             max_i = temp
# print(max_i)

# Решение группы
#

# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в
# качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует
# слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник
# заражен и нужно вывести номер холодильника, нумерация начинается с единицы
#
# Формат входных данных
# В первой строке подаётся число n – количество холодильников.
# В последующих строках вводятся строки, содержащие латинские строчные буквы и
# цифры, в каждой строке от 5 до 100 символов.
#
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет,
# ничего выводить не нужно.
import re

n = int(input('Введите кличество холодильников: '))
list1 = []
for i in range(n):
    inStr = input()
    if 'a' in inStr:
        inStr = inStr[inStr.find('a'):]
        if 'n' in inStr:
            inStr = inStr[inStr.find('n'):]
            if 't' in inStr:
                inStr = inStr[inStr.find('t'):]
                if 'o' in inStr:
                    inStr = inStr[inStr.find('o'):]
                    if 'n' in inStr:
                        list1.append(i + 1)
print(*list1)








