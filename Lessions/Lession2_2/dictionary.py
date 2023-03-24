# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу
# В списках в качестве ключа используется индекс элемента. В словарях для определения
# элемента используется значение ключа (строка, число)
"""
d = {}
d = dict()

d['q'] = 'qwerty'
print(d)                # {'q': 'qwerty'}
d['w'] = 'werty'
print(d)                # {'q': 'qwerty', 'w': 'werty'}
print(d['q'])           # qwerty
"""
# Пример

dictionary = {}
dictionary = {'up': '◘', 'left': '♦', 'down': '☻', 'right': '♠'}
print(dictionary)       # {'up': '◘', 'left': '♦', 'down': '☻', 'right': '♠'}
print(dictionary['left'])   # ♦
# типы ключей могут отличаться
dictionary[897] = 84648
print(dictionary)           # {'up': '◘', 'left': '♦', 'down': '☻', 'right': '♠', 897: 84648}

# Удаление элемента словаря
del dictionary[897]
print(dictionary)           # {'up': '◘', 'left': '♦', 'down': '☻', 'right': '♠'}

# Взаимодействие словарей с циклом for
for item in dictionary:
    print(item)         # Выведет только ключи в разных строках
    print('{}: {}'.format(item, dictionary[item]))          # Выведет пару - left: ♦

for (k, v) in dictionary.items():
    print(k, v)         # выведет пару ключ значение в формате - up ◘

print(dictionary.items())           # dict_items([('up', '◘'), ('left', '♦'), ('down', '☻'), ('right', '♠')])
