def Backtracking(path,obstacles,presentRow,presentColumn,destinationRow,destinationColumn):
    """
    At each recursive step, we will check whether the recursion reached the destination or not.
    If not, then we will check whether that present cell is a obstacle.
    If not, then we will mark the present cell as an obstacle so that the recursion couldn't come back to the same path.
    Then we will have a recursive call in all the four directions.
    We will un-mark the present cell as an obstacle.
    """
    if presentRow==destinationRow and presentColumn==destinationColumn:
        return [path]
    if obstacles[presentRow][presentColumn]==True:     # present cell is blocked
        return []
    obstacles[presentRow][presentColumn]=True          # marking the cell
    output=[]
    if presentRow<len(obstacles)-1:                    # DOWN
        output+=Backtracking(path+"D",obstacles,presentRow+1,presentColumn,destinationRow,destinationColumn)
    if presentColumn<len(obstacles[0])-1:              # RIGHT
        output+=Backtracking(path+"R",obstacles,presentRow,presentColumn+1,destinationRow,destinationColumn)
    if presentRow>0:                                   # UP
        output+=Backtracking(path+"U",obstacles,presentRow-1,presentColumn,destinationRow,destinationColumn)
    if presentColumn>0:                                # LEFT
        output+=Backtracking(path+"L",obstacles,presentRow,presentColumn-1,destinationRow,destinationColumn)
    obstacles[presentRow][presentColumn]=False         # un-marking the cell
    return output


obstacles=[[False,False,False],[False,False,False],[False,False,False]]
print(Backtracking("",obstacles,0,0,2,2))