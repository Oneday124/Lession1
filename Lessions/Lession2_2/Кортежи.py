# Кортеж - неизменяемый список
# Занимают меньше места в памяти и работают быстрее, чем списки
# Используют для защиты данных от изменений, например для хранения паролей

t = ()
print(type(t))              # <class 'tuple'>

t = (1, )
print(type(t))              # <class 'tuple'> Обязаиельно ", " после введенных данных

v = [1, 8, 9]
print(v)                    # [1, 8, 9]
print(type(v))              # <class 'list'>

v = tuple(v)
print(v)                    # (1, 8, 9)
print(type(v))              # <class 'tuple'>

# Разделение кортежа на переменные
a, b, c = v
print(a, b, c)              # 1 8 9

# Работа с кортежами
t = (1, 2, 3, 5,)
print(t[1])                 # 2

for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])

# t[0] = 2                    # TypeError: 'tuple' object does not support item assignment
