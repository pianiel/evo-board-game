# Board utilities class
# useful functions used both by the players and the game

class BoardUtils:

    # has to be even
    BOARD_SIZE = 8

    @staticmethod
    def prettyPrint (board):
        s = [[str(e) for e in row] for row in board]
        lens = [len(max(col, key=len)) for col in zip(*s)]
        fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print '\n'.join(table)
        print '\n'

    @staticmethod
    def gameFinished (board):
        for i in range(BoardUtils.BOARD_SIZE):
            for j in range(BoardUtils.BOARD_SIZE):
                if (BoardUtils.isLegalMove([i,j], board)):
                    return False
        return True

    @staticmethod
    def isLegalMove (move, board):
        if (move[0]>=BoardUtils.BOARD_SIZE or move[0]<0 or move[1]>=BoardUtils.BOARD_SIZE or move[1]<0):
            return False
        if (BoardUtils.isOccupied(move, board)):
            return False
        #TODO game rules...
        return True

    @staticmethod
    def isOccupied (field, board):
        if (board[field[0]][field[1]] == 0):
            return False
        return True

