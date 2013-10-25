#!/usr/bin/env python

# Human player, prompts for the move

from boardUtils import *
from src.gui.tkinter_demo import show_board_get_move

class HumanPlayer:
    def  __init__(self, name):
        self.name = name

    def move (self, board, myColor):
    	return show_board_get_move(board, myColor)

    def getName (self):
        return "HumanPlayer:" + self.name

    def __str__(self):
        return self.getName()
