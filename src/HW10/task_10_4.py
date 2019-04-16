# Имеется текстовый файл. Все четные строки записать
# во второй файл, а нечетные - в третий файл.
# Порядок следования строк сохраняется

def main():
    with open('test10_4_1.txt') as file1:
        with open('test10_4_2.txt') as file2:
            count = 1
            while True:
                line_file1 = file1.readline()
                line_file2 = file2.readline()

                if not line_file1:
                    break
                if line_file1 != line_file2:
                    print(f'line {count}')
                    break
                count += 1
        file2.close()
    file1.close()


if __name__ == '__main__':
    main()