"""
At every iteration, find the next maximum number and swap it with the next last position.
"""
def SelectionSort(array):
    for i in range(len(array)):
        lastindex=len(array)-i-1
        maxIndex=0
        for j in range(lastindex+1):
            if array[j]>array[maxIndex]:
                maxIndex=j
        array[maxIndex],array[lastindex]=array[lastindex],array[maxIndex]
    return array

def SelectionSortRecursive(array,iteration,position,maxNumPos):
    if iteration==0:
        return array
    if position<=iteration:
        if array[position]>array[maxNumPos]:
            return SelectionSortRecursive(array,iteration,position+1,position)
        else:
            return SelectionSortRecursive(array,iteration,position+1,maxNumPos)
    else:
        array[maxNumPos],array[position-1]=array[position-1],array[maxNumPos]
        return SelectionSortRecursive(array,iteration-1,0,0)

arr=[-5,5,-4,4,-3,3,-2,2,-1,1,0]
print(SelectionSort(arr))
print(SelectionSortRecursive(arr,len(arr)-1,0,0))