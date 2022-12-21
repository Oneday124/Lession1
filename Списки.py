ran = range(1,6)
print(type(ran))
numbers = list(ran)
print(numbers)
print(type(numbers))
print(f'{len(numbers)} len')

for i in numbers:
    i *= 2
    print(i)
print(numbers)

colors = ['red', 'green', 'blue']

for e in colors:
    print(e)                    # red green blue
for e in colors:
    print(e * 2)                # redred greengreen blueblue

colors.append('grey') # добавление элемента в конец списка
print(colors == ['red', 'green', 'blue', 'grey']) # True

colors.remove('red') #Удалить элемент из списка = del colors[0]
print(colors)

del colors[0]
print(colors)