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


