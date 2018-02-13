import itertools
import numpy as np
import pickle


class Bot:

    def __init__(self, training=True, save=True):
        self.scoring = {}  # A mapping of sums to point values
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

        self.dirName = [None] * 8  # Array of direction names
        self.dirs = [None] * 8  # Array that tracks which cells are in each dir

        self.dirName[0] = "top row"
        self.dirs[0] = [0, 1, 2]
        self.dirName[1] = "middle row"
        self.dirs[1] = [3, 4, 5]
        self.dirName[2] = "bottom row"
        self.dirs[2] = [6, 7, 8]
        self.dirName[3] = "left column"
        self.dirs[3] = [0, 3, 6]
        self.dirName[4] = "middle column"
        self.dirs[4] = [1, 4, 7]
        self.dirName[5] = "right column"
        self.dirs[5] = [2, 5, 8]
        self.dirName[6] = "forward diagonal"
        self.dirs[6] = [0, 4, 8]
        self.dirName[7] = "back diagonal"
        self.dirs[7] = [2, 4, 6]
        if training:
            self.d = {}
            self.d[4] = {}
            self.d[3] = {}
            self.d[2] = {}
            self.d[1] = {}
            i = 1
            for board in self.allNRevealedBoards(4):
                self.d[4][board] = self.bestChoiceLastStep(board)
                if (i % 20000 == 0):
                    print(board, self.d[4][board])
                i += 1
            for i in (3, 2, 1):
                for board in self.allNRevealedBoards(i):
                    self.d[i][board] = self.bestChoice(board, i)

            if save:
                file = open(r'/home/bobliang/Code/mini-cactpot/solution.pkl',
                            'wb')
                pickle.dump(self.d, file)
                file.close()
        else:
            file = open(r'/home/bobliang/Code/mini-cactpot/solution.pkl', 'rb')
            self.d = pickle.load(file)
            file.close()

    def allNRevealedBoards(self, N):
            # the four locations that have been flipped
            indicesList = list(itertools.combinations(range(9), N))
            revealedUnorderedList = list(itertools.combinations(range(1, 10), N))
            # the 4 revealed in order
            revealedList = []
            for revealedUnordered in revealedUnorderedList:
                revealedList += list(itertools.permutations(revealedUnordered))
            print(N, len(indicesList), len(revealedList))
            i = 0
            boards = []
            for indices in indicesList:
                for revealed in revealedList:
                    board = [" "] * 9
                    for i in range(N):
                        board[indices[i]] = revealed[i]
                    boards.append(tuple(board))            
            print(len(boards))
            return boards

    def bestOverallDir(self, boards):
        bestScore = 0
        bestDir = None
        for i in range(len(self.dirs)):
            dir = self.dirs[i]
            score = 0
            for board in boards:
                score += self.scoring[board[dir[0]] + board[dir[1]] +
                                      board[dir[2]]]
            if score > bestScore:
                bestDir = self.dirName[i]
                bestScore = score
        return (bestDir, bestScore/len(boards))

    def generateAllFilledBoards(self, board):
        boards = []
        indices = []
        missingNumbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for i in range(len(board)):
            if board[i] == " ":
                indices.append(i)
            else:
                missingNumbers.remove(board[i])

        permutations = list(itertools.permutations(missingNumbers))
        for permutation in permutations:
            newBoard = list(board)
            for i in range(len(indices)):
                newBoard[indices[i]] = permutation[i]
            boards.append(newBoard)
        return boards

    def bestChoiceLastStep(self, board):
        filledBoards = self.generateAllFilledBoards(board)
        return self.bestOverallDir(filledBoards)

    def bestChoice(self, board, N):
        boards = []
        indices = []
        missingNumbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for i in range(len(board)):
            if board[i] == " ":
                indices.append(i)
            else:
                missingNumbers.remove(board[i])
        bestScore = 0
        bestLoc = None
        for index in indices:
            expectedScore = 0
            for num in missingNumbers:
                newBoard = board[:index] + (num,) + board[index+1:]
                dir, score = self.d[N+1][newBoard]
                expectedScore += score
            if expectedScore/len(missingNumbers) > bestScore:
                bestScore = expectedScore/len(missingNumbers)
                bestLoc = index
        return (index, bestScore)

    def bestMove(self, board):
        numbers = set(board)
        N = len(numbers) - 1
        return self.d[N][board]

    def tileName(self, n):
        if n == 0:
            return "top left"
        elif n == 1:
            return "top"
        elif n == 2:
            return "top right"
        elif n == 3:
            return "left"
        elif n == 4:
            return "middle"
        elif n == 5:
            return "right"
        elif n == 6:
            return "bottom left"
        elif n == 7:
            return "bottom"
        elif n == 8:
            return "bottom right"
        else:
            return "error"
