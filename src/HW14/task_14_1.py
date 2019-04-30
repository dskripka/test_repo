from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age

    @abstractmethod
    def voice(self):
        print('')


class FelineInterface(ABC):
    @abstractmethod
    def climb_trees(self):
        pass

    @abstractmethod
    def scratch(self):
        pass


class CanineInterface(ABC):
    @abstractmethod
    def swimming(self):
        pass

    @abstractmethod
    def scent(self):
        pass


class Pet(Animal):
    pass  # Позволяет сохранить абстрактность от родительского класса


class WildAnimal(Animal):
    pass  # Позволяет сохранить абстрактность от родительского класса


class Cat(Pet, FelineInterface):
    def voice(self):
        print('Meow')

    def scratch(self):
        print('scratch')

    def climb_trees(self):
        print('climb_trees')


class Dog(Pet, CanineInterface):
    def voice(self):
        print('Gaw-Gaw')

    def scent(self):
        print('scent')

    def swimming(self):
        print('Swimming')


class Lion(WildAnimal, FelineInterface):
    def voice(self):
        print('RRRRRRRRRRRRR')

    def scratch(self):
        print('Scratch')

    def climb_trees(self):
        print('climb_trees')


class Wolf(WildAnimal, CanineInterface):
    def voice(self):
        print('U-U-U-U-U-U')

    def scent(self):
        print('scent')

    def swimming(self):
        print('Swimming')


def main():
    cat_1 = Cat(0.15, 3.5, 7)
    cat_1.climb_trees()
    cat_1.scratch()
    cat_1.voice()
    print('________________')

    dog_1 = Dog(15, 0.4, 2)
    dog_1.voice()
    dog_1.scent()
    dog_1.swimming()
    print('________________')

    lion_1 = Lion(80, 1.2, 6)
    lion_1.climb_trees()
    lion_1.scratch()
    lion_1.voice()
    print('________________')

    wolf_1 = Wolf(40, 0.7, 8)
    wolf_1.voice()
    wolf_1.scent()
    wolf_1.swimming()


if __name__ == '__main__':
    main()