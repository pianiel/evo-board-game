from Tkinter import Tk, Canvas, Frame, BOTH, Text, W, N, E, S
from ttk import Frame, Button, Label, Style

from src.model.boardgame.boardUtils import *

CH_BLACK = '#fb0'
CH_WHITE = '#05f'
CH_EMPTY = '#eee'
CH_POSSIBLE = '#f00'

class Example(Frame):
  
    def __init__(self, parent, board, myColor, circle_checkers=False):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.board = board
        self.myColor = myColor
        self.objIds = {}
        self.circle_checkers = circle_checkers
        self.initUI()

    def initUI(self):
      
        self.parent.title("Othello")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        

        canvas = Canvas(self, width=400, height=400)
        self.canvas = canvas
       
        self.createBoard()
        # self.redrawBoard(self.board)

        canvas.pack(fill=BOTH, expand=1)
        canvas.grid(row=1, column=0, columnspan=2, rowspan=4, 
            padx=5, sticky=E+W+S+N)
        
    def createBoard(self):
        n = 8
        c = 400/n # size of a square with checker
        d = c/10 # diameter of legal moves indicators
        pad = c/20
        for col in range(n):
            for row in range(n):
                ch_id = self.board[row][col]
                # print row, col, ch_id
                if ch_id == 1:
                    fill_color = CH_BLACK
                elif ch_id == 2:
                    fill_color = CH_WHITE
                else:
                    fill_color = CH_EMPTY
                isLegal = BoardUtils.isLegalMove([row,col], self.board, self.myColor)
                checker_id = self.canvas.create_rectangle(
                    1+row*c, 1+col*c, 1+(row+1)*c, 1+(col+1)*c,
                    outline="#000", fill=fill_color if not self.circle_checkers else CH_EMPTY)
                if self.circle_checkers and fill_color != CH_EMPTY:
                    self.canvas.create_oval(
                    1+row*c+pad, 1+col*c+pad, 1+(row+1)*c-pad, 1+(col+1)*c-pad,
                    outline="#000", fill=fill_color)
                if isLegal:
                    red_dot_id =self.canvas.create_oval(
                        1+row*c+(c-d)/2, 
                        1+col*c+(c-d)/2, 
                        1+(row+1)*c-(c-d)/2, 
                        1+(col+1)*c-(c-d)/2,
                        outline=CH_POSSIBLE, fill=CH_POSSIBLE)
                    # binding so a click on the red dot still selects the field
                    self.canvas.tag_bind(red_dot_id, '<ButtonPress-1>', self.onCheckerClick)
                    self.objIds[red_dot_id] = (row, col)
                self.canvas.tag_bind(checker_id, '<ButtonPress-1>', self.onCheckerClick)
                self.objIds[checker_id] = (row, col)
    
    def redrawBoard(self, board):
        n = 8
        for col in range(n):
            for row in range(n):
                ch_id = col*n+row + 1
                # print ch_id, ' ',
                ch_id = board[row][col]
                if ch_id == 1:
                    fill_color = CH_BLACK
                elif ch_id == 2:
                    fill_color = CH_WHITE
                else:
                    fill_color = CH_EMPTY
                self.canvas.itemconfigure(ch_id, fill_color)
        

    def onCheckerClick(self, event):
        # print 'Got click x=%d, y=%d' % (event.x, event.y)
        r, = event.widget.find_closest(event.x, event.y)
        print "r=", r
        n = 8
        row = (r-1) / n
        col = (r-1) % n
        row, col = self.objIds[r]
        print "row:", row
        print "col:", col
        # print "board:", self.board
        # print "mycolor:", self.myColor
        isLegal = BoardUtils.isLegalMove([row,col], self.board, self.myColor)
        print "islegal:", isLegal
        if isLegal:
            self.canvas.itemconfigure(r, fill=CH_BLACK)
            self.parent.chosen_move = [row, col]
            self.quit()


def show_board_get_move(board, myColor):
    print "asking human to move"
    root = Tk()
    root.geometry("412x402+200+100")
    app = Example(root, board, myColor, circle_checkers=False)
    root.mainloop()
    move = root.chosen_move
    print "Chosen_move:", move
    root.destroy()
    return move

def main():
    myColor = 2
    board = [[0 for x in xrange(BoardUtils.BOARD_SIZE)] for x in xrange(BoardUtils.BOARD_SIZE)] 
    show_board_get_move(board, myColor) 

if __name__ == '__main__':
    main()