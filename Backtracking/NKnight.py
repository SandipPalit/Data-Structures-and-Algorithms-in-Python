import copy

def NKnight(board,row,column,knight):
    """
    If we have placed all the Knights, then we will display the board.
    Else, for every column, we will check whether it is safe to place a Knight there.
    We will increment the column and if the cell reaches the rightmost cell of the board,
    then we will shift it to the leftmost cell of the next row.
    """
    if knight==0:
        for rows in board:
            for elements in rows:
                print(elements,end=" ")
            print()
        print()
        return
    if column==len(board) and row==len(board)-1:
        return
    if column==len(board):
        NKnight(board,row+1,0,knight)
        return
    if isSafe(board,row,column)==True:
        board[row][column]="K"
        NKnight(board,row,column+1,knight-1)
        board[row][column]="."
    NKnight(board,row,column+1,knight)

def isSafe(board,row,column):
    if row>=1 and column>=2 and board[row-1][column-2]=="K":            # Left-Left-Up
        return False
    if row>=2 and column>=1 and board[row-2][column-1]=="K":            # Up-Up-Left
        return False
    if row>=2 and column<len(board)-1 and board[row-2][column+1]=="K":  # Up-Up-Right
        return False
    if row>=1 and column<len(board)-2 and board[row-1][column+2]=="K":  # Right-Right-Up
        return False
    return True


NumberOfKnight=4
temp=[]
for i in range(NumberOfKnight):
    temp.append(".")
board=[]
for i in range(NumberOfKnight):
    board.append(copy.deepcopy(temp))
NKnight(board,0,0,NumberOfKnight)