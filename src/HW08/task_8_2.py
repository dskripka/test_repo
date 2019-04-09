# Дан список чисел. Посчитать сколько раз встречается каждое число

def counter(*args):
    count = {}
    for elem in args:
        if elem in count:
            count[elem] += 1
        else:
            count[elem] = 1
    for key, value in count.items():
        print(f'Number {key} occurs {value} times')

number = counter(20, 7, 1, 20, 5, 2, 8, 4, 7, 12, 6, 12, 2, 8, 1, 7, 1, 6, 5, 2, 6)
