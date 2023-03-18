# По данному целому не отрицательному n вычислите значение n!. N! = 1*2*3...*N
# Решить задачи используя цикл while.

# N = int(input('Введите n: '))
# i = 0
# factorial = 0
# while i <= N:
#     factorial += i
#     i += 1
# print(factorial)

# Дано натуральное число A < 1. Определите каким посчету числом фибаначи оно является, т.е выведите такое число N
# что ф(n) = A. Если А не является чслом фибаначи выведите 1.

A = int(input('Введите A: '))
old_n = 0
new_n = 1
fib = 1
i = 1
while fib < A:
    fib = old_n + new_n
    old_n = new_n
    new_n = fib
    i += 1

if A == fib:
    print(i)
else:
    print(-1)
