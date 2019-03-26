#Этот вариант решения я нашел и переделал, сам сделать не успевал.
fib1 = fib2 = 1
n = 15
while n < 2:
    print(fib1, end=' ')
    print(fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
print()
