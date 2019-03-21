summ =0
while True:
    number = input('Enter the string: \n')
    if number == 'stop':
        break
    if number.isdigit() and int(number) % 5 != 0:
        summ += int(number)
print(summ)
#TEST
