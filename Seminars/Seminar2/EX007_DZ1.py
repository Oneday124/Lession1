# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

number = input('Введите вещественное число: ')
result = 0
for i in set(number.replace('.', '')):
        result += int(i)
print(result)