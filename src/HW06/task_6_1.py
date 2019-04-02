# Написать программу, в которой вводятся два операнда X и Y и знак операции
# (+ - * /)
# вычисить результат в зависимости от знака.предусмотреть реакции на
# неверный знак операцииа также на ввод 0 при делении

i = 5
possible_sign = ['+', '-', '*', '/', '0']
while i > 0:

    x = int(input('Insert the X: \n'))
    y = int(input('Insert the Y: \n'))
    sign = input('Insert + - * / or 0 = stop  \n')

    if y == 0 and sign == '/':
        print('Division by "0" is impossible!')
        continue

    if sign in possible_sign:
        if sign == '0':
            break
        if sign == '+':
            result = x + y
        if sign == "-":
            result = x - y
        if sign == '*':
            result = x * y
        if sign == '/':
            result = x / y
        print(result)
    else:
        print('Invalid operation sign!!!')