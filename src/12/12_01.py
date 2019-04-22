class Cat:
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

    def meow(self):
        print('meow')



class Dog:
    def __init__(self, name, age, master):
        self.__name = name
        self.__age = age
        self.__master = master

    def run(self):
            print('run')

    def jump(self):
            print('jump')

    def birthday(self):
        self.age += 1

    def bark(self):
        print('Gau gau')

class Parrot:
    def __init__(self, name, age, master):
        self.__name = name
        self.__age = age
        self.__master = master

        def run(self):
            print('run')

        def jump(self):
            print('jump')

        def birthday(self):
            self.age += 1

        def fly(self):
            print('fly')

    def fly(self):
        print('fly')

    cat = Cat('Barsik', 3, 'Dmitry')
    dog = Dog('Bobik', 5, 'Vova')
    parrot= Parrot('Moisha', 15, 'Abram' )
