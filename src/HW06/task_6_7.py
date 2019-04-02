#Дана целочисленная квадратная матрица. Найти в каждой строке наи-
#больший элемент и поменять его местами с элементом главной диагонали.

from random import randint

n = int(input('n: '))

matrix = []

for i in range(0, n):
    row = []
    for j in range(0, n):
        row.append(randint(1, 9))
    matrix.append(row)
print(matrix)

for i in range(0, n):
#    row = ' '.join(matrix[i])
    print(row)
d = [matrix[i][i] for i in range(len(matrix))]
print(d)

for i in range(0, n):
    max_el = 0
    for j in range(0, n):
        if matrix[i][j] > max_el:
            max_el = matrix[i][j]
            matrix[i][i] = max_el
    print(max_el)
for i in range(n):
    print(matrix[i])
