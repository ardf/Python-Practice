# Import Module
from tkinter import *


def rowComplete(row):
  # Tests if a row is all equal to 1 or 0
  if row[0] != "-" and all(element == row[0] for element in row):
    return row[0]
  else:
    return None


def getColumn(matrix, index):
  # Gets a column from the matrix
  return [row[index] for row in matrix]


def getDiagonal(matrix, descend):
  # Gets a diagnol line from the matrix
  out = []
  for i in range(3):
    row = matrix[i]
    out += row[2 - i if descend else i]
  return out
    

def codeToWinner(code):
  # Simply gets who won, A or B
  return "A" if code == '0' else "B"


def validateMatrix(matrix):
  # Validates a matrix to ensure it's good to work on
  A_count = 0
  B_count = 0
  if len(matrix) != 3:
    # If there are more than three rows
    return False
  for row in matrix:
    if len(row) != 3:
      # If there are more than three cells in a row
      return False
    for cell in row:
      if cell == "0":
        A_count += 1
      elif cell == "1":
        B_count += 1
      elif cell != "-":
        # If a cell contains a value other than 1, 0, or "-"
        return False
  diff = A_count - B_count
  # Ensure that no player has played more moves than they're supposed to
  return diff <= 1 and diff >= -1


def evaluateWinner(matrix):
  # Vaidate our matrix
  if not validateMatrix(matrix):
    return "-1"

  # See if any rows are complete
  for row in matrix:
    winner = rowComplete(row)
    if winner is not None:
      return codeToWinner(winner)

  # See if any columns are complete
  for i in range(0, 3):
    col = getColumn(matrix, i)
    winner = rowComplete(col)
    if winner is not None:
      return codeToWinner(winner)

  # See if any diagnols are complete
  winner = rowComplete(getDiagonal(matrix, False))
  if winner is not None:
    return codeToWinner(winner)
  winner = rowComplete(getDiagonal(matrix, True))
  if winner is not None:
    return codeToWinner(winner)
  
  # If nothing was complete, then our game is incomplete
  return "0"


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
