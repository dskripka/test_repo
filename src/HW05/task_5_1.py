# Создать квадратную матрицу размерностью n и заполнить ее
# случайными значениями. Найти сумму всех элементов матрицы,
# которые кратны 3.
# __________________________________________
#1) Дана целочисленная матрица размера 5х5. Получить новую матрицу
#путем деления всех элементов данной матрицы на ее наибольший по
#модулю элемент.[02-4.2-ML-17]

# Примечание: не успел доделать.

from random import randint

n = 5

matrix = []
max_el = 0
for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(-999, 999))
    matrix.append(row)
    if matrix[i][j] > max_el:
        max_el = abs(matrix[i][j])
print(max_el)
print(matrix)

matrix_new = []
for i in range(n):
    matrix_new = matrix[i][j] / max_el
print(matrix_new)

