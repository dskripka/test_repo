# Написать программу, со следующим интерфейсом: пользователю предоставляется на выбор 12 вариантов
# перевода(описанных в первой задаче). Пользователь вводит цифру от одного до двенадцати. После
# программа запрашивает ввести численное значение. Затем программа выдает конвертированный результат.
# Использовать функции из первого задания. Программа должна быть в бесконечном цикле.
# Код выхода из программы - “0”


# Convert Inches to Centimeters
def inch_to_cm(z):
    rezult = z * 2.54
    return rezult


# Convert Centimeters to Inches
def cm_to_inch(z):
    rezult = z / 2.54
    return rezult


# Convert Miles to Kilometers
def mil_to_km(z):
    rezult = z * 1.60934
    return rezult


# Convert Kilometers to Miles
def km_to_mil(z):
    rezult = z / 1.60934
    return rezult


# Convert Pounds to Kilograms
def pound_to_kg(z):
    rezult = z * 0.45359237
    return rezult


# Convert Kilograms to Pounds
def kg_to_pound(z):
    rezult = z / 0.45359237
    return rezult


# Convert Grams to Ounces
def oz_to_gram(z):
    rezult = z * 31.1034768
    return rezult


# Convert Ounces to Grams
def gram_to_oz(z):
    rezult = z / 31.1034768
    return rezult


# Convert Gallons to Liters
def gal_to_litres(z):
    rezult = z * 3.785411784
    return rezult


# Convert Liters to Gallons
def litres_to_gal(z):
    rezult = z / 3.785411784
    return rezult


# Convert Pints to Liters
def pints_to_litres(z):
    rezult = z * 0.568261485
    return rezult


# Convert Liters to Pints
def litres_to_pints(z):
    rezult = z / 0.568261485
    return rezult



while True:
    welcome_screen = (

        '                                      \n'
        'Welcome to the unit converter program.\n'
        '                                      \n'
        ' 1 - Convert Inches to Centimeters \n'
        ' 2 - Convert Centimeters to Inches \n'
        ' 3 - Convert Miles to Kilometers \n'
        ' 4 - Convert Kilometers to Miles \n'
        ' 5 - Convert Pounds to Kilograms \n'
        ' 6 - Convert Kilograms to Pounds \n'
        ' 7 - Convert Grams to Ounces \n'
        ' 8 - Convert Ounces to Grams \n'
        ' 9 - Convert Gallons to Liters \n'
        '10 - Convert Liters to Gallons \n'
        '11 - Convert Pints to Liters \n'
        '12 - Convert Liters to Pints \n'
    )
    print(welcome_screen)
    type_value = int(input('Choose type of Convertible Value: '))
    if type_value == 0:
        print('Exit the program')
        break
    if type_value not in range(1, 13):
        print('Incorrect Type')
        continue
    input_data = int(input('Enter a Value: \n'))
    if type_value == 1:
        rez = inch_to_cm(input_data)
    elif type_value == 2:
        rez = cm_to_inch(input_data)
    elif type_value == 3:
        rez = mil_to_km(input_data)
    elif type_value == 4:
        rez = km_to_mil(input_data)
    elif type_value == 5:
        rez = pound_to_kg(input_data)
    elif type_value == 6:
        rez = kg_to_pound(input_data)
    elif type_value == 7:
        rez = oz_to_gram(input_data)
    elif type_value == 8:
        rez = gram_to_oz(input_data)
    elif type_value == 9:
        rez = gal_to_litres(input_data)
    elif type_value == 10:
        rez = gal_to_litres(input_data)
    elif type_value == 11:
        rez = pints_to_litres(input_data)
    elif type_value == 12:
        rez = litres_to_pints(input_data)
    print(rez)