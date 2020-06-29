
class Player:

    __name = ''
    __number = 0

    def __init__(self, name, number):
        self.__name = name;
        self.__number = number;
        pass

    def getName(self):
        return self.__name;

    def getNumber(self):
        return self.__number;