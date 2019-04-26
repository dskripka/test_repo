from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def voice(self):
        print('')

class FelineInterface(ABC):
    @abstractmethod
    def scratch(self):
        pass


class CanineInterface(ABC):
    @abstractmethod
    def swimming(self):
        pass

class Pet(Animal):
    pass                # Позволяет сохранить абстрактность от родительского класса

class WildAnimal(Animal):
    pass                # Позволяет сохранить абстрактность от родительского класса


class Cat(Pet):
    def voice(self, FelineInterface):
        print('Meow')


class Dog(Pet):
    def voice(self, CanineInterface):
        print('Gaw-Gaw')


class Lion(WildAnimal):
    def voice(self, FelineInterface):
        print('RRRRRRRRRRRRRR')


class Wolf(WildAnimal):
    def voice(self, CanineInterface):
        print('')

