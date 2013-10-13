# Game class
# Represents the current state of the board and logic behind the game
# Calls players passed to the constructor when it is their time to move

# Both players and tokens:
# 1 = black
# 2 = white

from boardUtils import *
from veryDumbPlayer import *

class IllegalMoveException(Exception):
    def __init__(self, move):
        self.move = move
    def __str__(self):
        return "Illegal Move Exception: Trying to put token in "+str(self.move[0])+ ","+ str(self.move[1])

class Game:

    def __init__(self, blackPlayer, whitePlayer):
        self.board = [[0 for x in xrange(BoardUtils.BOARD_SIZE)] for x in xrange(BoardUtils.BOARD_SIZE)] 
        self.nextPlayer = 1
        self.blackPlayer = blackPlayer
        self.whitePlayer = whitePlayer
        self.board[BoardUtils.BOARD_SIZE/2][BoardUtils.BOARD_SIZE/2] = 1
        self.board[BoardUtils.BOARD_SIZE/2-1][BoardUtils.BOARD_SIZE/2-1] = 1
        self.board[BoardUtils.BOARD_SIZE/2][BoardUtils.BOARD_SIZE/2-1] = 2
        self.board[BoardUtils.BOARD_SIZE/2-1][BoardUtils.BOARD_SIZE/2] = 2
    
    def play (self):
        while (not BoardUtils.gameFinished(self.board)):
            move = [-1,-1]
            if (self.nextPlayer == 1):
                move = self.blackPlayer.move(self.board, self.nextPlayer)
            else:
                move = self.whitePlayer.move(self.board, self.nextPlayer)
            if (BoardUtils.isLegalMove(move, self.board)):
                self.makeMove(move)
            else:
                raise IllegalMoveException(move)
            BoardUtils.prettyPrint(self.board)
        #TODO return winner? notify winners?


    def makeMove (self, move):
        self.board[move[0]][move[1]] = self.nextPlayer
        self.nextPlayer = self.nextPlayer % 2 + 1

print "Let's play a game..."
game = Game(VeryDumbPlayer(), VeryDumbPlayer())
try:
    game.play()
except IllegalMoveException as e:
    print e
