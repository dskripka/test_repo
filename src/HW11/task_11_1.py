def main():

    class Home:
        def __init__(self, lengt, width, height, number_of_floors):
            self.__lengt = lengt
            self.__width = width
            self.__height= height
            self.__number_of_floors = number_of_floors

        def get_lengt(self):
            return self.__lengt

        def set_lengt(self, lengt):
            self.__lengt = lengt

        def get_width(self):
            return self.__width

        def set_width(self, width):
            self.__width = width

        def get_height(self):
            return self.__height

        def set_height(self, height):
            self.__height = height

        def get_number_of_floors(self):
            return self.__number_of_floors

        def set_number_of_floors(self, number_of_floors):
            self.__number_of_floors = number_of_floors

    home1 = Home(100000, 15000, 35000, 12)

    class Window:
        def __init__(self, width, height, thickness):
            self.__width = width
            self.__height = height
            self.__thickness = thickness

        def get_width(self):
                return self.__width

        def set_width(self, width):
                self.__width = width

        def get_height(self):
                return self.__height

        def set_height(self, height):
                self.__height = height

        def get_thickness(self):
                return self.__thickness

        def set_thickness(self, thickness):
                self.__thickness = thickness

    window1 = Window(1200, 1800, 4)

    class Door:
        def __init__(self, width, height, thickness, material):
            self.__width = width
            self.__height = height
            self.__thickness = thickness
            self.__material = material

        def get_width(self):
                return self.__width

        def set_width(self, width):
                self.__width = width

        def get_height(self):
                return self.__height

        def set_height(self, height):
                self.__height = height

        def get_thickness(self):
                return self.__thickness

        def set_thickness(self, thickness):
                self.__thickness = thickness

        def get_material(self):
                return self.__material

        def set_thickness(self, material):
                self.__material = material

    door1 = Door(2100, 700, 60, 'Wood')

    class Table:
        def __init__(self, width, height, depth):
            self.__width = width
            self.__height = height
            self.__depth = depth

        def get_width(self):
            return self.__width

        def set_width(self, width):
            self.__width = width

        def get_height(self):
            return self.__height

        def set_height(self, height):
            self.__height = height

        def get_depth(self):
            return self.__depth

        def set_thickness(self, depth):
            self.__depth = depth

    table1 = Table(1200, 900, 750)

    class Cat:
        def __init__(self, name, height, weight, age, color):
            self.__name = name
            self.__height = height
            self.__weight = weight
            self.__age = age
            self.__color = color

        def get_name(self):
            return self.__name

        def set_name(self, name):
            self.__name = name

        def get_height(self):
            return self.__height

        def set_height(self, height):
            self.__height = height

        def get_weight(self):
            return self.__weight

        def set_weight(self, weight):
            self.__height = weight

        def get_age(self):
            return self.__age

        def set_age(self, age):
            self.__age = age

        def get_color(self):
            return self.__age

        def set_age(self, color):
            self.__color = color

    cat1 = Cat('Vasily', 210, 6, 8, 'striped')

if __name__ == '__main__':
    main()
