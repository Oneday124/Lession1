text = 'съешь еще этих мягких французских булок'
print(text[0])                  # c
print(text[1])                  # ъ
#print(text[len(text)])         # IndexError
print(text[len(text) - 1])      # к
print(text[-5])                 # б - пятый с конца
print(text[:])                  # съешь еще этих мягких французских булок - вывод текста целиком [:] = text[0:len(text) - 1]
print(text[len(text) - 2:])     # ок
print(text[2:9])                # ешь еще - со 2 по 9
print(text[6:-18])              # еще этих мягких
print(text[0:len(text):6])      # сеикакл
print(text[::6])                # сеикакл
text = text[2:9] + text[-5] + text[:2]
print(text)                     # ешь ещебсъ