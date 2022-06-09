def BacktrackingWithPathMatrix(path,obstacles,pathMatrix,stepCount,presentRow,presentColumn,destinationRow,destinationColumn):
    """
    At each recursive step, we will check whether the recursion reached the destination or not.
    If not, then we will check whether that present cell is a obstacle.
    If not, then we will mark the present cell as an obstacle so that the recursion couldn't come back to the same path.
    We will assign the next stepCount to the path matrix to track the traversal.
    Then we will have a recursive call in all the four directions.
    We will un-mark the present cell as an obstacle.
    """
    if presentRow==destinationRow and presentColumn==destinationColumn:
        pathMatrix[presentRow][presentColumn]=stepCount
        print(path)
        for row in pathMatrix:
            print(row)
        print()
        return
    if obstacles[presentRow][presentColumn]==True:     # present cell is blocked
        return
    obstacles[presentRow][presentColumn]=True          # marking the cell
    pathMatrix[presentRow][presentColumn]=stepCount
    if presentRow<len(obstacles)-1:                    # DOWN
        BacktrackingWithPathMatrix(path+"D",obstacles,pathMatrix,stepCount+1,presentRow+1,presentColumn,destinationRow,destinationColumn)
    if presentColumn<len(obstacles[0])-1:              # RIGHT
        BacktrackingWithPathMatrix(path+"R",obstacles,pathMatrix,stepCount+1,presentRow,presentColumn+1,destinationRow,destinationColumn)
    if presentRow>0:                                   # UP
        BacktrackingWithPathMatrix(path+"U",obstacles,pathMatrix,stepCount+1,presentRow-1,presentColumn,destinationRow,destinationColumn)
    if presentColumn>0:                                # LEFT
        BacktrackingWithPathMatrix(path+"L",obstacles,pathMatrix,stepCount+1,presentRow,presentColumn-1,destinationRow,destinationColumn)
    obstacles[presentRow][presentColumn]=False         # unmarking the cell
    pathMatrix[presentRow][presentColumn]=0


pathMatrix=[[0,0,0],[0,0,0],[0,0,0]]
obstacles=[[False,False,False],[False,False,False],[False,False,False]]
BacktrackingWithPathMatrix("",obstacles,pathMatrix,0,0,0,2,2)