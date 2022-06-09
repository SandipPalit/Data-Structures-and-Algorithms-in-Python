def BinarySearchRowAndColumnSorted(array,target):
    """
    The input array is Row-wise and Column-wise sorted.
    Here, we will start checking from 0-th row and last column.
    If that element is equal to target, then return the index.
    If that element is greater than target, then drop that column.
    If that element is less than target, then drop that row.
    """
    row=0
    column=len(array[0])-1
    while row<len(array) and column>=0:
        if array[row][column]==target:
            return [row,column]
        elif array[row][column]>target:
            column-=1
        else:
            row+=1
    return [-1,-1]


def BinarySearchSortedMatrix(array,target):
    """
    Initially we will search in the middle column.
    If element is equal to target, then return the index.
    If element is greater than target, then drop the rows below that element.
    If element is less than target, then drop the rows above that element.

    Now we will have only two rows.

    We will check if the middle column of both the rows, contain the target. If yes, then return the index.
    Else, we will divide them into 4 1D array and then perform normal binary search.
    Part 1: Top row, from 0-th Column to mid-1 column
    Part 2: Top row, from mid+1 Column to last column
    Part 3: Bottom row, from 0-th Column to mid-1 column
    Part 4: Bottom row, from mid+1 Column to last column
    """
    rowsCount=len(array)
    columnsCount=len(array[0])
    if rowsCount==0 or columnsCount==0:
        return [-1,-1]
    if rowsCount==1:
        rowNumber=0
        columnStart=0
        columnEnd=columnsCount-1
    else:
        rowStart=0
        rowEnd=rowsCount-1
        columnMid=columnsCount//2
        while rowStart<rowEnd-1:
            rowMid=(rowEnd+rowStart)//2
            if array[rowMid][columnMid]==target:
                return [rowMid][columnMid]
            elif target>array[rowMid][columnMid]:
                rowStart=rowMid
            else:
                rowEnd=rowMid
        # Now two rows remaining
        if array[rowStart][columnMid]==target:
            return [rowStart,columnMid]
        if array[rowEnd][columnMid]==target:
            return [rowEnd,columnMid]
        if array[rowStart][0]<=target<array[rowStart][columnMid]:
            # 1st part
            rowNumber=rowStart
            columnStart=0
            columnEnd=columnMid-1
        elif array[rowStart][columnMid]<target<=array[rowStart][columnsCount-1]:
            # 2nd part
            rowNumber=rowStart
            columnStart=columnMid+1
            columnEnd=columnsCount-1
        elif array[rowEnd][0]<=target<array[rowEnd][columnMid]:
            # 3rd part
            rowNumber=rowEnd
            columnStart=0
            columnEnd=columnMid-1
        else:
            # 4th part
            rowNumber=rowEnd
            columnStart=columnMid+1
            columnEnd=columnsCount-1
    while columnStart<=columnEnd:
        columnMid=(columnStart+columnEnd)//2
        if array[rowNumber][columnMid]==target:
            return [rowNumber,columnMid]
        elif target>[rowNumber][columnMid]:
            columnStart=columnMid+1
        else:
            columnEnd=columnMid-1
    return [-1,-1]


array1=[[10,20,30,40],
        [15,25,35,45],
        [28,29,37,49],
        [33,34,38,50]]

array2=[[11,12,13,14],
        [15,16,17,18],
        [19,20,21,22],
        [23,24,25,26]]

print(BinarySearchRowAndColumnSorted(array1,37))
print(BinarySearchSortedMatrix(array2,23))