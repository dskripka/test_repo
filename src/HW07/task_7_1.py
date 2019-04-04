#    1. Написать 12 функций по переводу:
#    1. Дюймы в сантиметры
#    2. Сантиметры в дюймы
#    3. Мили в километры
#    4. Километры в мили
#    5. Фунты в килограммы
#    6. Килограммы в фунты
#    7. Унции в граммы
#    8. Граммы в унции
#    9. Галлон в литры
#    10. Литры в галлоны
#    11. Пинты в литры
# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на выбор 12 вариантов
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

#print(litres_to_pints(1))
