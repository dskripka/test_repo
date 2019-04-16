#  Имеется текстовый файл. Переписать в другой файл все его строки
# с заменой в них символа 0 на символ 1 и наоборот.

def main():
    with open('test10_2_1.txt') as my_file:
        with open('test10_2_2.txt', 'w') as new_my_file:
            while True:
                line = list(my_file.readline())
                if not line:
                    break
                new_line = []
                for elem in line:
                    if elem == '0':
                        elem = '1'
                    elif elem == '1':
                        elem = '0'
                    new_line.append(elem)
                new_my_file.writelines(new_line)
            new_my_file.close()
        my_file.close()

if __name__ == '__main__':
    main()
