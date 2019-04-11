#Создать lambda функцию, которая принимает на вход
#неопределенное количество именных аргументов и выводит
#словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}


def my_func(**kwargs):
    old_dict = kwargs
    for key, value in old_dict.items():
        new_dict = {key * 2: value for key, value in old_dict.items()}
    print(new_dict)
my_func(abc = 1, defgh = 2, ijkl = 3, mno = 4, pqrs = 5, tu = 6, xy = 7, z = 8)


