
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print("Пожалуй, хватит") # Когда условие перестает выполняться
print(inverted)