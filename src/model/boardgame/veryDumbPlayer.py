# VERY dumb player trying to put a token in the first empty field it sees
# WILL cause illegal move exceptions once proper game logic is implemented

from boardUtils import *

class VeryDumbPlayer:
    def  __init__(self):
        pass

    def move (self, board, myColor):
        for i in range (BoardUtils.BOARD_SIZE):
            for j in range (BoardUtils.BOARD_SIZE):
                if (not BoardUtils.isOccupied([i,j], board)):
                    return [i,j]

