#Добавить в класс Pet пустой метод voice.
# Заменить имена методов bark, meow на voice.
# Создать функцию, принимающая список животных
# и вызывающая у каждого животного метод voice.

def main():

    from pets import Pet, Dog, Cat, Parrot


    def voice(*args):
        for animal in args:
            if animal == 'dog':

                dog.voice()
            elif animal == 'cat':
                cat.voice()

            dog = Dog('Bobik', 5, 'Vova', 35, 430)

            cat = Cat('Barsik', 3, 'Dmitry', 4, 210)
            cat.voice()

        print(voice('dog', 'cat'))

if __name__ == '__main__':
    main()