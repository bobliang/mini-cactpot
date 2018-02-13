from Board import Board
from Player import Player
from Bot import Bot
import numpy as np

board = Board()
player = Player()

while(True):
    board.reveal(np.random.randint(0, 3), np.random.randint(0, 3))
    board.display()
    x = input("Cheats on? ([y]/n)")
    if x == "n":
        cheats = False
    else:
        bot = Bot(training=False, save=False)
        print("bot loaded")
        cheats = True

    if(cheats):
        move, ev = bot.bestMove(board.linearize())
        print("reveal", bot.tileName(move), "with ev", ev)

    x = input("Flip tile: ")
    board.niceReveal(x)
    board.display()


    if(cheats):
        move, ev = bot.bestMove(board.linearize())
        print("reveal", bot.tileName(move), "with ev", ev)

    x = input("Flip tile: ")
    board.niceReveal(x)
    board.display()

    if(cheats):
        move, ev = bot.bestMove(board.linearize())
        print("reveal", bot.tileName(move), "with ev", ev)

    x = input("Flip tile: ")
    board.niceReveal(x)
    board.display()

    if(cheats):
        move, ev = bot.bestMove(board.linearize())
        print("choose", move, "with ev", ev)

    x = input("Score direction: ")
    score = board.score(x)
    board.display()
    print("Score direction:", x)
    print("Your score is", score[0][0], "+", score[0][1], "+", score[0][2],
          "=", score[0][0] + score[0][1] + score[0][2], "=>", score[1])
    player.addScore(score[1])
    print("You have played", player.timesPlayed(), "times.")
    print("Your average score is", player.averageScore())
    x = input("Play again? ([y]/n) ")
    if (x == "n"):
        break
    board = Board()
