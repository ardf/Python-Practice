# Import Module
from tkinter import *

def createRootWindow(self):    
    # root window title and dimension
    self.title("TicTacToe")
    self.resizable(0,0)

    # get the screen dimension
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    # all widgets will be here
    createGameBoard()

    # Execute Tkinter

def createGameBoard():
    gameBoard = Frame(root, bg="#000")
    gameBoardHeight = window_height / 2
    gameBoardWidth = window_width / 2
    gameBoard.place(x=window_width/4, y=window_height/4,width=gameBoardWidth,height=gameBoardHeight)
    board = Frame(gameBoard)
    board.place(x=gameBoardWidth/10, y= gameBoardHeight/10)
    button1=Button(board, cursor="circle", height=5, width=10, text="")
    button1.grid(row=0,column=0)

    button2=Button(board, cursor="circle", height=5, width=10, text="")
    button2.grid(row=0,column=1)

    button3=Button(board, cursor="circle", height=5, width=10, text="")
    button3.grid(row=0,column=2)

    button4=Button(board, cursor="circle", height=5, width=10, text="")
    button4.grid(row=1,column=0)

    button5=Button(board, cursor="circle", height=5, width=10, text="")
    button5.grid(row=1,column=1)

    button6=Button(board, cursor="circle", height=5, width=10, text="")
    button6.grid(row=1,column=2)

    button7=Button(board, cursor="circle", height=5, width=10, text="")
    button7.grid(row=2,column=0)

    button8=Button(board, cursor="circle", height=5, width=10, text="")
    button8.grid(row=2,column=1)

    button9=Button(board, cursor="circle", height=5, width=10, text="")
    button9.grid(row=2,column=2)
    
#create root window
root = Tk()
window_width = 600
window_height = 600
createRootWindow(root)
root.mainloop()
