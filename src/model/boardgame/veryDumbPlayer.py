# Very Dumb player, returns first legal move it sees

from boardUtils import *

class VeryDumbPlayer:
    def  __init__(self):
        pass

    def move (self, board, myColor):
        for i in range (BoardUtils.BOARD_SIZE):
            for j in range (BoardUtils.BOARD_SIZE):
                if (BoardUtils.isLegalMove([i,j], board, myColor)):
                    return [i,j]
