class Dog:
    def __init__(self, name, height, weight, age, master, address):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__master = master
        self.__address = address



    @property
    def master(self):
        return self.__master

    @property
    def name(self):
        return self.__name

    @property
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

    @property
    def age(self):
        return self.__age

    @property
    def address(self):
        return self.__address


    @master.setter
    def master(self, master):
        return self.__master

    @name.setter
    def name(self, name):
        return self.__name

    @height.setter
    def height(self, height):
        return self.__height

    @weight.setter
    def weight(self, weight):
        return self.__weight

    @age.setter
    def age(self, age):
        return self.__age

    @address.setter
    def address(self, address):
        return self.__address




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
#print(dog1.get_master()) # Вызывваем метод get_master()
#dog1.set_address('Grodno') # Вызывваем метод get_address()
print(dog1.get_address())


dog2 = Dog('Sharik', 350, 22, 8, 'Arkady', 'Bobruysk')

print(dog2.name)
print(dog2.height)
print(dog2.weight)
print(dog2.age)
