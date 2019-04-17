#Изменение атрибутов

class Dog:
   def change_height(self, height):
       self.height = height

dog_1 = Dog('Bob', 11, 12, 2015)
print(dog_1.height)
dog_1.change_height(15)
print(dog_1.height)