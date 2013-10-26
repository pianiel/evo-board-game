#!/usr/bin/env python

# Game class
# Represents the current state of the board and logic behind the game
# Calls players passed to the constructor when it is their time to move

# Both players and tokens:
# 1 = black
# 2 = white

from boardUtils import *
from veryDumbPlayer import *
from humanPlayer import *

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
        self.winner = None
        self.loser = None
        self.whitePlayer = whitePlayer
        self.board[BoardUtils.BOARD_SIZE/2][BoardUtils.BOARD_SIZE/2] = 1
        self.board[BoardUtils.BOARD_SIZE/2-1][BoardUtils.BOARD_SIZE/2-1] = 1
        self.board[BoardUtils.BOARD_SIZE/2][BoardUtils.BOARD_SIZE/2-1] = 2
        self.board[BoardUtils.BOARD_SIZE/2-1][BoardUtils.BOARD_SIZE/2] = 2
    
    def play (self):
        while (not BoardUtils.gameFinished(self.board)):
            move = [-1,-1]
            if not BoardUtils.hasMove(self.board, self.nextPlayer):
                self.nextPlayer = BoardUtils.otherPlayer(self.nextPlayer)
            if (self.nextPlayer == 1):
                move = self.blackPlayer.move(self.board, self.nextPlayer)
            else:
                move = self.whitePlayer.move(self.board, self.nextPlayer)
            if (BoardUtils.isLegalMove(move, self.board, self.nextPlayer)):
                self.makeMove(move)
            else:
                raise IllegalMoveException(move)
            #BoardUtils.prettyPrint(self.board)
        winner = BoardUtils.determineWinner(self.board, self.nextPlayer)
        if (winner == 1):
            self.winner=self.blackPlayer
            self.loser=self.whitePlayer
        elif (winner == 2):
            self.winner=self.whitePlayer
            self.loser=self.blackPlayer

    def getWinner (self):
        return self.winner

    def getLoser (self):
        return self.loser

    def makeMove (self, move):
        self.board = BoardUtils.applyMove(move, self.board, self.nextPlayer)
        self.nextPlayer = BoardUtils.otherPlayer(self.nextPlayer)

if __name__ == '__main__':
    #example usage:
    print "Let's play a game..."

    player1 = VeryDumbPlayer("Zygfryd")
    player2 = VeryDumbPlayer("Szczepan")
    game = Game(player1, player2)
    try:
        game.play()
        if not game.getWinner() == None:
            print "The winner is:", game.getWinner().getName()
        else:
            print "Draw!"
    except IllegalMoveException as e:
        print e
