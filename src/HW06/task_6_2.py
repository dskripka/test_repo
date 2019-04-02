#Дано число. Найти сумму и произведение его цифр.

number = input('Enter number: \n')
list = [int(i) for i in list(number)]
print(list)
summ = sum(list)
print(summ)
product = 1
for x in list:
    product *= x
print(product)