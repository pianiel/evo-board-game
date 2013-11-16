from Tkinter import Tk, Canvas, Frame, BOTH, Text, W, N, E, S
from ttk import Frame, Button, Label, Style

from src.model.boardgame.boardUtils import *

CH_BLACK = '#fb0'
CH_WHITE = '#05f'
CH_EMPTY = '#eee'

class Example(Frame):
  
    def __init__(self, parent, board, myColor):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.board = board
        self.myColor = myColor
        self.objIds = {}
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
        
        # lbl = Label(self, text="Othello")
        # lbl.grid(sticky=W, pady=4, padx=5)
        
        canvas = Canvas(self, width=400, height=400)
        self.canvas = canvas
        # bounds = canvas.bbox()
        # width = bounds[2] - bounds[0]
        # height = bounds[3] - bounds[1]
        # print 'width', width
        # print 'height', height
        self.createBoard()
        # self.redrawBoard(self.board)

        canvas.pack(fill=BOTH, expand=1)
        canvas.grid(row=1, column=0, columnspan=2, rowspan=4, 
            padx=5, sticky=E+W+S+N)
        
        # abtn = Button(self, text="Play", command=self.play)
        # abtn.grid(row=1, column=3)

        # cbtn = Button(self, text="Close")
        # cbtn.grid(row=2, column=3, pady=4)
        
        # hbtn = Button(self, text="Help")
        # hbtn.grid(row=5, column=0, padx=5)

        # obtn = Button(self, text="OK")
        # obtn.grid(row=5, column=3)        
    
    def createBoard(self):
        n = 8
        ch_dim = 400/n
        ch_w = ch_dim
        ch_h = ch_dim
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
                checker_id = self.canvas.create_rectangle(
                    1+row*ch_w, 1+col*ch_h, 1+(row+1)*ch_w, 1+(col+1)*ch_h,
                    outline="#000", fill=fill_color)
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


    def play(self):
        print "play?"
        self.parent.chosen_move = "asdasdasda"
        # self.quit()


def show_board_get_move(board, myColor):
    print "asking human to move"
    root = Tk()
    root.geometry("412x402+200+100")
    app = Example(root, board, myColor)
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