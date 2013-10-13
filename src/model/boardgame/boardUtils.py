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
    def gameFinished (board, nextMoveColor):
        for i in range(BoardUtils.BOARD_SIZE):
            for j in range(BoardUtils.BOARD_SIZE):
                if (BoardUtils.isLegalMove([i,j], board, nextMoveColor)):
                    return False
        return True

    @staticmethod
    def isLegalMove (move, board, color):
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

    @staticmethod
    def otherPlayer (player):
        return player % 2 + 1

    #we assume that the game is finished
    @staticmethod
    def determineWinner (board, nextMoveColor):
        nextPlayers = 0
        previousPlayers = 0
        for row in board:
            for field in row:
                if (field == nextMoveColor):
                    nextPlayers = nextPlayers + 1
                if (field == BoardUtils.otherPlayer(nextMoveColor)):
                    previousPlayers = previousPlayers + 1;
                if (field == 0):
                    #there are still blank fields, but next player has no legal move to make (because the game is finished)
                    return BoardUtils.otherPlayer(nextMoveColor)
        if (nextPlayers > previousPlayers):
            return nextMoveColor
        if (nextPlayers < previousPlayers):
            return BoardUtils.otherPlayer(nextMoveColor)
        return 0
                
