# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &,|,^
# is, is not, in, not in

a = 1 < 4 and 5 > 2
print(a)

b = 1 == 2
print(b)

c = "awe"
e = "awe"
print(c == e)

i = [1,2]
j = [1,2]
print(i == j) # Списки сравниваются по элементно

g = 1 < 3 < 5 # можно использовать двойные, тройные и т.д неравенства
print(g)

f = [1,2,3,4]
print(f)
print(2 in f) #проверяет есть ли элемент в списке
print(not 2 in f)

is_odd = not f[0] % 2  #f[0] % 2 == 0
print(is_odd)