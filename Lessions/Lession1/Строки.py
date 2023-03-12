text = 'съешь еще этих мягких французских булок'
print(len(text))                    # 39 - количество символов в строке
print('еще' in text)                # True - поиск совпадений (наличие подстроки в строке)
print(text.isdigit())               # False - являются ли все символы в строке числами
print(text.islower())               # True - являются ли все символы в строке символами в нижнего регистра
print(text.upper())                 # СЪЕШЬ ЕЩЕ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК - все символы в верхнем регистре
print(text.lower())                 # съешь ЕЩЕ этих мягких французских булок - все символы в нижнем регистре
print(text.replace('еще', 'ЕЩЕ'))   # Замена

# вызов подсказок по встроенным методам

help(text.lower)