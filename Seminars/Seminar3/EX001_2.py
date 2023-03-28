# Дан список чисел, определить сколько в нем различных чисел

# arr = [1, 1, 2, 0, -1, 3, 4, 4, 7, 8, -3]
# arr2 = set()
# for i in arr:
#     arr2.add(i)
# print(len(arr2))

# решение группы:

# arr = [1, 1, 2, 0, -1, 3, 4, 4, 7, 8, -3]
# arr2 = []
#
# for j in range(len(arr)):
#     if j not in arr2:
#         arr2.append(arr[j])
# print(arr2)

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательнось
# на K элементов вправо, K - положительное число
# k = int(input('Введите K: '))
# j = -k
# arr = [1, 2, 3, 4, 5]
# for i in arr:
#     print(arr[j])
#     j += 1

# решение группы

# arr = [1, 2, 3, 4, 5]
# k = int(input('Введите K: '))
# print(f'{arr[len(arr)-k:len(arr)] + arr[:len(arr)-k]}')

# решение группы 2

# arr = [1, 2, 3, 4, 5]
# k = int(input('Введите K: '))
# for i in range(k):
#     arr.insert(0, arr.pop(-1))
# print(arr)

# Напишите программу для печати всех уникальных значений в словаре
# input [{'V':'S001'},{'V':'S002'},{'VI':'S001'},{'VI':'S005'},{'VII':'S005'},{'V':'S009'},{'VIII':'S007'}]
# Output {'S005','S002','S007','S001','S009'}
dictionary = {'V ': 'S001', ' V': 'S002', ' VI': 'S001', 'VI': 'S005', 'VII': 'S005', ' V ': 'S009', 'VIII': 'S007'}
new_list = set()

for item in dictionary:
    print(dictionary[item])
    new_list.add(dictionary[item])
print(new_list)

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего
# input [0,-1,5,2,3]
# output 2

# arr = [0, -1, 5, 2, 3]
#
# count = 0
# for i in range(len(arr)):
#     if arr[i] > arr[i-1]:
#         count += 1
#
# print(count)