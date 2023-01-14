# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1

n = int(input('Введите натуральное число n: '))
dictionary = {}
for i in range(n):
    dictionary[i + 1] = 3 * (i + 1) + 1
print(dictionary)