# Написать функцию, которая принимает список строк и возвращает список строк, содержащих только одно слово,
# с использованием лямбда-функции:
# strings = ["Hello, world!", "This is a sentence.", "Another sentence", "Hello,", "sentence.", "Another"]
# strings = ["Hello,", "sentence.", "Another"]

strings = ["Hello, world!", "This is a sentence.", "Another sentence", "Hello,", "sentence.", "Another"]

string1 = list(filter(lambda x: len(x.split()) == 1, strings))
print(string1)

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic -
# это функция, которая принимает объект и вычисляет его характеристику.
