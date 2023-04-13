# Модуль OS
# Модуль OS предоставляет множество функций для работы с операционной системой, причем
# их поведение, как правило, не зависит от OS, поэтому программы остаются переносимыми

# Для того, чтобы начать работать с данным модулем необходимо его импортировать в свою программу:
# import os

# Базовые функции модуля:
# os.chdir(path) -  смена текущей директории
# os.getcwd() - текущая рабочая директория

import os
print(os.getcwd())              # C:\Users\Саша\Desktop\Обучение\Python\Lessions\Lession4

# os.path - является вложенным модулем в модуль os и реализует некоторые полезные функции для работы с путями,
# такие как:

# os.path.basename(path) - базовое имя пути

import os
print(os.path.basename('C:/Users/Саша/Desktop/Обучение/Python/Lessions/Lession4/Library OS.py')) # Library OS.py

# os.path.abspath(path) - возвращает нормализованный абсолюьный путь

import os
print(os.path.abspath('Library OS.py')) # C:\Users\Саша\Desktop\Обучение\Python\Lessions\Lession4\Library OS.py
