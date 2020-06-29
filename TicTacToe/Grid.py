
class Grid:

    __dimension = 0
    __grid = []

    def __init__(self, dimension):
        for i in range(0, self.__dimension):
            self.__grid.append([])
        pass

    def printGrid(self):

        self.__grid = [[" _" for x in range(self.__dimension)]]

        for y in range(self.__dimension):
            
            row = []
            for x in range(self.__dimension * 2 + 1):
                if x % 2 == 0:
                    row.append("|")
                else:
                    row.append("_")
            self.__grid.append(row)

        for row in self.__grid:
            print("".join(row))

        pass