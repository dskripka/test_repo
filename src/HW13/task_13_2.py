# Создать класс Book. Атрибуты: количество страниц,
# год издания, автор, цена.
# Добавить валидацию в конструкторе на ввод
# корректных данных. Создать иерархию ошибок.


class Book:

    def __init(self, name, author, year, pages):
        self.author = author
        self.pages = pages

        if pages < 0:
            raise Exception
        self.name = name
        if year > 2016:
            raise Exception
        self.year = year


def main():
    try:
        book_1 = Book('Python Programming', 'John Zelle', 2016, 552)

    except Exception:
        print('something is wrong !!!!')

    print('End program')


if __name__ == '__main__':
    main()
