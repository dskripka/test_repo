#Абстрактный класс
#Абстрактный класс - класс, экземпляр которого нельзя создать.

from abc import ABC, abstractmethod

class A(ABC):
   @abstractmethod
   def do_smth(self):
       print('I am a parent')
class B(A):
   def do_smth(self):
       print('I am a child')
a = A() # ERROR
b = B()
