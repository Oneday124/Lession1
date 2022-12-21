a = 123
b = 1.23
#print(type(a)) # Вывод типов
#print(type(b))
s = 'Hello, word'
#print(s) #вывод строки
i = 'Hello,\' word'
#print(i) #вывод строки c '
j = 'Hello,\n word'
#print(j) #вывод строки c переходом на новую строку

#Интерполяция (вывод нескольких переменных в одну строку)
print(a,b,s)
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a,b,s)) #форматированный вывод
print(f'{a} - {b} - {s}') #Интерполяция
print('{1} - {2} - {0}'.format(a,b,s))

f = True
print(f)

list = [1,2,3] #Создание массива
print(list)

print('Введите а: ')
a = int(input())
print(a)
print(type(a))



