


class King:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def show(self):
        print('---------------------')
        print('name :', self.name)
        print('year :', self.year)

if __name__ == '__main__':

    king1 = King('태조', 1392)
    king2 = King('태종', 1392)
    king3 = King('세종대왕', 1418)

    king1.show()
    king2.show()
    king3.show()
