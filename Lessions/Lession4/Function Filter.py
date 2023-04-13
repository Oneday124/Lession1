data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

data = '15 156 96 3 5 8 52 5'

data = list(map(int, data.split()))
print(data)

# заменим функцию where из прошлой задачи с листа Lambda Function на функцию filter (так как это одно и то же)

# def where(f, col):
#     return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]

res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
