# Кортеж - неизменемый список
t = ()
print(type(t))      # Tuple

t = (1,)
print(type(t))      # Tuple

t = (1)
print(type(t))      # int

t = (28, 9, 1990)
print(type(t))      # tuple

colors = ['red', 'blue', 'green']           # Список
print(colors)       # ['red', 'blue', 'green']

t = tuple(colors)                           # Кортеж
print(t)       # ['red', 'blue', 'green']
print(t[0])    # red
print(t[2])    # green
print(t[-2])   # blue

t = tuple(['red', 'blue', 'green'])
red, blue, green = t
print('r:{} q:{} b:{}'.format(red, blue, green))


a = (3, 1, 41, 4)
# print(a)
# print(a[-2])

for item in a:
    print(item)