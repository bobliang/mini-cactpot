import numpy as np


class Board:
    def __init__(self):
        self.data = np.random.permutation(9).reshape((3, 3)) + 1
        self.visible = [[" " for i in range(3)] for j in range(3)]
        self.scoring = {}
        self.scoring[6] = 10000
        self.scoring[7] = 36
        self.scoring[8] = 720
        self.scoring[9] = 360
        self.scoring[10] = 80
        self.scoring[11] = 252
        self.scoring[12] = 108
        self.scoring[13] = 72
        self.scoring[14] = 54
        self.scoring[15] = 180
        self.scoring[16] = 72
        self.scoring[17] = 180
        self.scoring[18] = 119
        self.scoring[19] = 36
        self.scoring[20] = 306
        self.scoring[21] = 1080
        self.scoring[22] = 144
        self.scoring[23] = 1800
        self.scoring[24] = 3600

    def linearize(self):
        result = []
        for sublist in l:
            for item in sublist:
                    result.append(item)
        return result

    def display(self):
        for i in range(40):
            print("")
        print(" MINI  CACTPOT ")
        print("*=============*")
        print("||", self.visible[0][0], "|", self.visible[0][1], "|",
              self.visible[0][2], "||")
        print("||---|---|---||")
        print("||", self.visible[1][0], "|", self.visible[1][1], "|",
              self.visible[1][2], "||")
        print("||---|---|---||")
        print("||", self.visible[2][0], "|", self.visible[2][1], "|",
              self.visible[2][2], "||")
        print("*=============*")
        print("")
        print("Scoring:")
        for i in range(6, 10):
            print(i, "   ", self.scoring[i])
        for i in range(10, 25):
            print(i, "  ", self.scoring[i])

    def niceReveal(self, square):
        if square == "top left":
            self.reveal(0, 0)
        elif square == "top":
            self.reveal(0, 1)
        elif square == "top right":
            self.reveal(0, 2)
        elif square == "left":
            self.reveal(1, 0)
        elif square == "middle":
            self.reveal(1, 1)
        elif square == "right":
            self.reveal(1, 2)
        elif square == "bottom left":
            self.reveal(2, 0)
        elif square == "bottom":
            self.reveal(2, 1)
        elif square == "bottom right":
            self.reveal(2, 2)

    def reveal(self, x, y):
        self.visible[x][y] = self.data[x][y]

    def score(self, direction):
        total = 0
        if direction == "top row":
            cells = [(0, 0), (0, 1), (0, 2)]
        elif direction == "middle row":
            cells = [(1, 0), (1, 1), (1, 2)]
        elif direction == "bottom row":
            cells = [(2, 0), (2, 1), (2, 2)]
        elif direction == "left column":
            cells = [(0, 0), (1, 0), (2, 0)]
        elif direction == "middle column":
            cells = [(0, 1), (1, 1), (2, 1)]
        elif direction == "right column":
            cells = [(0, 2), (1, 2), (2, 2)]
        elif direction == "forward diagonal":
            cells = [(0, 0), (1, 1), (2, 2)]
        elif direction == "back diagonal":
            cells = [(0, 2), (1, 1), (2, 0)]

        data = []
        for (a, b) in cells:
            self.reveal(a, b)
            data.append(self.data[a][b])
            total += self.data[a][b]

        return (data, self.scoring[total])
