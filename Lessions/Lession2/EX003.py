# Функции

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5))       # !!!!!
print(new_string('!'))          #TupeError missing I required ...
print(new_string(4))

# Неограниченное количество переменных

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w'))
