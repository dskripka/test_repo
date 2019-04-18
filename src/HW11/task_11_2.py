#Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5)
#стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости).
# Все атрибуты приватные.

def main():

    class Car:
        def __init__(self, marque, model, year, speed):
            self.__marque = marque
            self.__model = model
            self.__year = year
            self.__speed = speed

        def get_marque(self):
            return self.__marque

        def get_model(self):
            return self.__model

        def get_year(self):
            return self.__year

        def get_speed(self):
            return self.__speed

        def set_speed(self, speed):
            self.__speed = speed


    car1 = Car('Shkoda', 'Oktavia', 1997, 10)

    print(car1.get_marque())
    print(car1.get_model())
    print(car1.get_year())
    print(car1.get_speed())
    print(' ')
    car1.set_speed((car1.get_speed()) + 5)         # Speed increase by 5
    print(car1.get_speed())
    car1.set_speed((car1.get_speed()) - 5)         # Speed reduction by 5
    print(car1.get_speed())
    car1.set_speed((car1.get_speed()) * (-1))      # Change the direction of movement
    print(car1.get_speed())
    car1.set_speed(0)                              # Speed reset (Stop)
    print(car1.get_speed())

if __name__ == '__main__':
    main()
