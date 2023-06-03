# import pandas as pd
# Чтение
# df = pd.read_csv('simple_data/california_housing_train.csv', sep=',')
# Показать скрытые входные данные (defoult = 5)
# df.head(n = 10)  # 10 - кол-во строк
# Вывод последних элементов таблицы (n - кол-во строк с конца)
# df.tail(n = 10)
# Общий размер таблицы
# df.shape     # (17000, 9)
# Просмотр пустых значений
# df.isnull()
# Подсчет пустых значений по столбцам
# df.isnull().sum()
# Тип данных столбца
# df.stypes
# df.columns    #Index(['longitude', 'latitude', 'housing_median_age', 'total_rooms', ... , ' median_house_value'],
                #       dtype='object')

# Выборка данных
# Вывод столбцов
# df[['latitude', 'populations']]
# Вывод стоблца с условием
# df[df['houseing_median_age'] < 20]
# Выборка по определенному условию и вывод только определенного столбца
# df[df['houseing_median_age'] < 20]['total_rooms']
# Выборка по нескольким условиям
# df[(df['houseing_median_age'] < 20) & (df['houseing_median_age'] > 10)][['total_rooms', 'houseing_median_age']]

# Простая статистика
# максимальное значение по столбцу
# print(df['population']. max())
# print(df['population']. min())    # минимальное
# print(df['population']. mean())   # среднее
# print(df['population']. sum())    # сумма по столбцу

# df[['population', 'total_rooms']].median()    # медиана от двух столбцов
# Получение всей информации сразу
# df.describe()
# count - общее кол-во не пустых строк
# mean - среднее значение в столбце
# std - стандартное отклонение от среднего значения
# min - минимальное значение
# max - максимальное значение
# числа 25%, 50%, 75% - перцентили
# Перцентиль - показатель, используемый в статистике, показывающи значение ниже которого палает определенный процент
# наблюдений в группе наблюдений

# Изображение статистических отношений
# Scatterplot (точечный график)
# import seaborn as sns
# Изображение точек долготы по отношению к широте:
# sns.scatterplot(data=df, x = 'longitude', y = 'latitude')
# Отношение, чем выше количество семей, тем выше кол-во людей и соответственно комнат (hue - оттенок)
# sns.scatterplot(data=df, x = 'households', y = 'population', hue = 'total_rooms')
# size - размер точек
# sns.scatterplot(data=df, x = 'households', y = 'population', hue = 'total_rooms', size = 10)
# Визуализация сразу нескольких отношений, используя класс PairGrid внутри seadorn.
# PairGrid принимает как аргумент pandas DataFrame и виуализирует все возможные отношения между ними, в соответствии
# с выбранным типом графика
# cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
# g = sns.PairGrid(df[cols]
# g.map(sns.scatterplot)

# Линейные графики
# Хорошо подойдут, если есть временная или какая-либо иная последовательность и значения, которые могут меняться в
# зависимости от нее. Для генерации линейных графиков в seaborn используется relplot функция. Она принимает
# DataFrame , x, y - столбцы
# sns.relplot(x = 'latitude', y = 'median_house_value', kind = 'line', data = df

# Гистограмма
# sns.histplot(data = df, x = 'median_income')

# Разбивка данных на группы
# df.loc[df['house_median_age'] <= 20, 'age_group'] = 'Молодые'
# df.loc[(df['house_median_age'] > 20) & (df['house_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
# df.loc[df['house_median_age'] > 50, 'age_group'] = 'Пожилые'

# группировка таблицы по параметру age_group и построение графика
# df.groupby('age_group')['median_income'].mean().plot(kind='bar')

