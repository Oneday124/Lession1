# Более глубокая теория работы со списками
list1 = [1, 2, 3, 4, 5]
list2 = list1

for e in list1:
    print(e)

print()

for e in list2:
    print
list1[0] = 123
list2[1] = 333
for e in list1:
    print(e)

print()

for e in list2:
    print(e)

list1 = [1, 2, 3, 4, 5]

print(list1.pop(2))         # удаление конкретного элемента их списка (в примере - с индексом 2)
print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())

print(list1.insert(2, 11))         # добавление элемента в список (на позицию с инд 2 доюавляем 11
print(list1)

print(list1.append(111))         # добавление элемента в конец списка
print(list1)