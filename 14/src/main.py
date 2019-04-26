from random import randint


class Matrix():
    def __init__(self, data=None):
        if not data:                        #Если нет входных данных
            data = []
            self.n = self.m = 5
            for i in range(5):
                row = []
                for j in range(5):
                    row.append(randint(0, 9))
                data.append(row)
        else:
            self.n = len(data)
            self.m = len(data[0])
        self.data = data




