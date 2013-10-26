#!/usr/bin/env python

# Board utilities class
# useful functions used both by the players and the game

import copy

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
        return not (BoardUtils.hasMove(board, 1) or BoardUtils.hasMove(board, 2))

    @staticmethod
    def hasMove (board, nextMoveColor):
        for i in range(BoardUtils.BOARD_SIZE):
            for j in range(BoardUtils.BOARD_SIZE):
                if (BoardUtils.isLegalMove([i,j], board, nextMoveColor)):
                    return True
        return False
    
    @staticmethod
    def isLegalMove (move, board, color):
        if not BoardUtils.liesWithinBoard(move, board):
            return False
        if BoardUtils.isOccupied(move, board):
            return False
        if BoardUtils.canFlip(move, board, color, 1, 1):
            return True
        if BoardUtils.canFlip(move, board, color, 1, 0):
            return True
        if BoardUtils.canFlip(move, board, color, 1, -1):
            return True
        if BoardUtils.canFlip(move, board, color, 0, -1):
            return True
        if BoardUtils.canFlip(move, board, color, -1, -1):
            return True
        if BoardUtils.canFlip(move, board, color, -1, 0):
            return True
        if BoardUtils.canFlip(move, board, color, -1, 1):
            return True
        if BoardUtils.canFlip(move, board, color, 0, 1):
            return True
        return False
    
    @staticmethod
    def liesWithinBoard (field, board):
        if (field[0]>=BoardUtils.BOARD_SIZE or field[0]<0 or field[1]>=BoardUtils.BOARD_SIZE or field[1]<0):
            return False
        return True
        
    #we assume that the move is legal
    @staticmethod
    def applyMove (move, board, color):
        newBoard = copy.deepcopy(board)
        newBoard[move[0]][move[1]] = color
        if BoardUtils.canFlip (move, newBoard, color, 1, 1):
            BoardUtils.flip (move, newBoard, color, 1, 1)
        if BoardUtils.canFlip (move, newBoard, color, 1, 0):
            BoardUtils.flip (move, newBoard, color, 1, 0)
        if BoardUtils.canFlip (move, newBoard, color, 1, -1):
            BoardUtils.flip (move, newBoard, color, 1, -1)
        if BoardUtils.canFlip (move, newBoard, color, 0, 1):
            BoardUtils.flip (move, newBoard, color, 0, 1)
        if BoardUtils.canFlip (move, newBoard, color, 0, -1):
            BoardUtils.flip (move, newBoard, color, 0, -1)
        if BoardUtils.canFlip (move, newBoard, color, -1, 1):
            BoardUtils.flip (move, newBoard, color, -1, 1)
        if BoardUtils.canFlip (move, newBoard, color, -1, 0):
            BoardUtils.flip (move, newBoard, color, -1, 0)
        if BoardUtils.canFlip (move, newBoard, color, -1, -1):
            BoardUtils.flip (move, newBoard, color, -1, -1)
        return newBoard
    
    #we assume that we can flip
    @staticmethod
    def flip (field, board, color, dx, dy):
        i = 1
        while (BoardUtils.liesWithinBoard ([field[0]+i*dx, field[1]+i*dy], board) and board[field[0]+i*dx][field[1]+i*dy] == BoardUtils.otherPlayer(color)):
            board[field[0]+i*dx][field[1]+i*dy] = color
            i = i+1

    @staticmethod
    def canFlip (field, board, color, dx, dy):
        nextField = [field[0]+dx, field[1]+dy]
        if not BoardUtils.liesWithinBoard (nextField, board):
            return False
        if not board[nextField[0]][nextField[1]] == BoardUtils.otherPlayer(color):
            return False
        i = 2
        while (BoardUtils.liesWithinBoard ([field[0]+i*dx, field[1]+i*dy], board) and board[field[0]+i*dx][field[1]+i*dy] == BoardUtils.otherPlayer(color)):
            i = i+1
        if (BoardUtils.liesWithinBoard ([field[0]+i*dx, field[1]+i*dy], board) and board[field[0]+i*dx][field[1]+i*dy] == color):
            return True
        return False

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
        if (nextPlayers > previousPlayers):
            return nextMoveColor
        if (nextPlayers < previousPlayers):
            return BoardUtils.otherPlayer(nextMoveColor)
        return 0
                
