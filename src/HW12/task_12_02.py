#Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы сравнения,
# сложения, вычитания, умножения на число, вывод на экран.
# Перегрузить конструктор на обработку входных параметров
# вида: одна строка, три числа, другой объект класса
# MyTime, и отсутствие входных параметров.

from datetime import datetime, date, time, timedelta

def main():

    class MyTime:
        def __init__(self, hours, minutes, seconds):
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    my_time = MyTime(10, 20, 55)

if __name__ == '__main__':
    main()
