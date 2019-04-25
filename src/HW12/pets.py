class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True

    def run(self):
        print('run')

    def jump(self):
        print('jump')

    def birthday(self):
        self.age += 1

    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight +=0.2



class Cat(Pet):
    def meow(self):
        print('meow')

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 16:
                self.is_alive = False



class Dog(Pet):
    def bark(self):
        print('Gau gau')

    def birthday(self):
        super().birthday()
        if self.age > 13:
            self.is_alive = False


class Parrot(Pet):
    def fly(self):
        print('fly')

    def birthday(self):
        super().birthday()
        if self.age > 60:
            self.is_alive = False

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