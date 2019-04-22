#Перегрузка методов
#Перегрузка метода позволяет менять логику выполнения метода в зависимости от типа и количества переданных аргументов.


class Dog:
    def __init__(self, name):
        self.name = name

    def set_name(self, name=None):
        if name:
            self.name = name
        else:
            print('Name was not changed')


dog1 = Dog('Vasya')
dog1.set_name('Bob')