def SudokuSolver(board):
    """
    We will find the first Empty cell. Then we will place a number from 1 to 9 and and recursively repeat this step
    to solve this sudoku. It it cannot solve the sudoku then we will backtrack and place another number.
    """
    row=-1
    column=-1
    emptyCellFound=False
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c]==0:                                              # empty cell found
                row=r
                column=c
                emptyCellFound=True
                break
        if emptyCellFound==True:
            break
    if emptyCellFound==False:                                               # sudoku solved
        return True
    for number in range(1,10):
        if isSafe(board,row,column,number):
            board[row][column]=number
            if SudokuSolver(board)==True:
                return True
            else:
                board[row][column]=0
    return False

def isSafe(board,row,column,number):
    for i in range(len(board)):                                             # checking Row
        if board[i][column]==number:
            return False
    for i in range(len(board)):                                             # checking Column
        if board[row][i]==number:
            return False
    squareRootOfBoardLength=int(len(board)**(1/2))
    rowStart=row-(row % squareRootOfBoardLength )
    columnStart=column-(column % squareRootOfBoardLength )
    for r in range(rowStart,rowStart+squareRootOfBoardLength):            # checking Small squares
        for c in range(columnStart,columnStart+squareRootOfBoardLength):
            if board[r][c]==number:
                return False
    return True


board=[[3, 0, 6, 5, 0, 8, 4, 0, 0],
       [5, 2, 0, 0, 0, 0, 0, 0, 0],
       [0, 8, 7, 0, 0, 0, 0, 3, 1],
       [0, 0, 3, 0, 1, 0, 0, 8, 0],
       [9, 0, 0, 8, 6, 3, 0, 0, 5],
       [0, 5, 0, 0, 9, 0, 6, 0, 0],
       [1, 3, 0, 0, 0, 0, 2, 5, 0],
       [0, 0, 0, 0, 0, 0, 0, 7, 4],
       [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if SudokuSolver(board)==True:
    for rows in board:
        for elements in rows:
            print(elements,end=" ")
        print()
else:
    print("Cannot solve this Sudoku!!")