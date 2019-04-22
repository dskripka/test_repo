#Вызов родительского метода

class A:
   def do_something(self):
       print('AA')
class B(A):
   def do_something(self):
       super(B, self).do_something()
       print('BB')

