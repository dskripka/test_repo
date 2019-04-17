class Dog:
    def __init__(self, name, height, weight, age, master, address):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.__master = master
        self.__address = address


    def get_master(self):
        return self.__master

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


    def change_height(self, height):
        self.height = height

    def change_name(self, name):
        self.name = name

    def jump(self):
        print('Jump')

    def run(self):
        print('Run')

    def bark(self):
        print('Woof Woof!')



dog1 = Dog('Bobik', 300, 15, 4, 'Valera', 'Minsk')

print(dog1.name)
print(dog1.height)
print(dog1.weight)
print(dog1.age)
print(dog1.get_master()) # Вызывваем метод get_master()
dog1.set_address('Grodno') # Вызывваем метод get_address()
print(dog1.get_address())


dog2 = Dog('Sharik', 350, 22, 8, 'Arkady', 'Bobruysk')

print(dog2.name)
print(dog2.height)
print(dog2.weight)
print(dog2.age)
