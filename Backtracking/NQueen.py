import copy

def NQueen(board,row):
    """
    If we have placed Queens in all the rows, then we will display the board.
    Else, for every column, we will check whether it is safe to place a Queen there.
    If Yes, then we will place a Queen there and move to the next row.
    """
    if row==len(board):
        for rows in board:
            for elements in rows:
                print(elements,end=" ")
            print()
        print()
        return
    for column in range(len(board)):
        if isSafe(board,row,column)==True:
            board[row][column]="Q"
            NQueen(board,row+1)
            board[row][column]="."

def isSafe(board,row,column):
    for i in range(row):                                # checking vertical
        if board[i][column]=="Q":
            return False
    for i in range(1,min(row,column)+1):                # checking left diagonal
        if board[row-i][column-i]=="Q":
            return False
    for i in range(1,min(row,len(board)-column-1)+1):   # checking right diagonal
        if board[row-i][column+i]=="Q":
            return False
    return True

NumberOfQueen=4
temp=[]
for i in range(NumberOfQueen):
    temp.append(".")
board=[]
for i in range(NumberOfQueen):
    board.append(copy.deepcopy(temp))
NQueen(board,0)