from abc import ABC, abstractmethod
class Pet(ABC):
    __counter = 0
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__counter += 1

    @abstractmethod
    def voice(self):
        pass

    @classmethod
    def get_counter(cls):
        return cls.__counter

    def run(self):
        print('run')

    def jump(self):
        print('jump')

    def birthday(self):
        self.age += 1

#    def change_weight(self):
#        self.weight

    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight +=0.2



class Cat(Pet):
    def voice(self):
        print('meow')


class Dog(Pet):
    def voice(self):
        print('Gau gau')


class Parrot(Pet):
    def fly(self):
        print('fly')

    def voice(self):
        print('Karr-Karr')

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height +=0.05

    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight +=0.05

class Horse(Pet):
    def voice(self):
        print('IGOGO')

class Donkey(Pet):
    def voice(self):
        print('IA-IA-IA')

class Mule(Donkey, Horse):
    pass

cat = Cat('Barsik', 3, 'Dmitry', 4, 210)
dog = Dog('Bobik', 5, 'Vova', 35, 430)
parrot = Parrot('Moisha', 15, 'Abram', 0.05, 15)
mule = Mule('Moisha', 15, 'Abram', 0.05, 15)

mule.voice()

print(parrot.weight)
parrot.change_weight()
print(parrot.weight)
print(cat.name)
print(dog.name)
cat.change_weight(20)

