class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

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
    def meow(self):
        print('meow')


class Dog(Pet):
    def bark(self):
        print('Gau gau')


class Parrot(Pet):
    def fly(self):
        print('fly')

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



cat = Cat('Barsik', 3, 'Dmitry', 4, 210)
dog = Dog('Bobik', 5, 'Vova', 35, 430)
parrot = Parrot('Moisha', 15, 'Abram', 0.05, 15)
print(parrot.weight)
parrot.change_weight()
print(parrot.weight)
print(cat.name)
cat.meow()
print(dog.name)
cat.change_weight(20)