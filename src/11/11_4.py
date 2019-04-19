#Создать класс Dog. Класс имеет четыре атрибута: name, height, weight, age.
# Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение
# на экран. Создать два объекта класса Dog, вызвать все методы у каждого объекта.


class Dog:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age


    def jump(self):
        print('Jump')

    def run(self):
        print('Run')

    def bark(self):
        print('Woof Woof!')

dog1 = Dog('Bobik', 300, 15, 4)

print(dog1.name)
print(dog1.height)
print(dog1.weight)
print(dog1.age)

dog2 = Dog('Sharik', 350, 22, 8)

print(dog2.name)
print(dog2.height)
print(dog2.weight)
print(dog2.age)
