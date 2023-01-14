# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите N: '))
factorial = 1
for i in range(n):
    factorial *= i + 1
    print(factorial, end = ' ')