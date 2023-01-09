# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}             # Пустой словарь
dictionary = \
    {
        'up': '',
        'left': '-',
        'down': ',',
        'right': '*'
    }
print(dictionary)
print(dictionary['left'])
dictionary['left'] = '!'
print(dictionary['left'])
# Типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k)
#
# for v in dictionary.values():
#     print(v)
#
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

