# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.

from random import randint
n = 19
row = []
max_el = 0
for i in range(n):
    row.append(randint(0, 999))
print(row)
print(max(row))
for n, i in enumerate(row):
    if i % 2 == 0:
        row[n] = (max(row))
print(row)
