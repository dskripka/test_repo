class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('run')

    def jump(self):
        print('jump')

    def birthday(self):
        self.age += 1


class Cat(Pet):
    def meow(self):
        print('meow')


class Dog(Pet):
    def bark(self):
        print('Gau gau')


class Parrot(Pet):
    def fly(self):
        print('fly')


cat = Cat('Barsik', 3, 'Dmitry')
dog = Dog('Bobik', 5, 'Vova')
parrot = Parrot('Moisha', 15, 'Abram')

print(cat.name)
cat.meow()
print(dog.name)
