#Для заданного числа N составьте программу вычисления суммы
#S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.

n = int(input('Insert the n: \n'))
i = 2
a = 1
while i <= n:
    s = a + (1 / i)
    a = a + s
    a = s
    i += 1
print(s)

