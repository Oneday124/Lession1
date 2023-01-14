# Вывести цвет кармана на колесе рулетки (0 - 36). Краман 0 - зеленый
# 1 - 10 чет черный, нечет красный
# 11 - 18 чет красный, нечет черный
# 19 - 28 чет черный, нечет красный
# 29 - 36 чет красный, нечет черный

print('Введите номер кормана: ')
number = int(input())
if number == 0:
    print("Зеленый")
elif number >= 1 and number <= 10 or number >= 19 and number <= 28:
    if number % 2 == 0:
        print("Черный")
    else:
        print("Красный")
elif number >= 11 and number <= 18 or number >= 29 and number <= 36:
    if number % 2 == 0:
        print("Красный")
    else:
        print("Черный")
else:
    print("Ошибка ввода")