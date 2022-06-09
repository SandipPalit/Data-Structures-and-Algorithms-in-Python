def BubbleSort(array):
    """
    For every element, if the previous element is greater than the present element, then swap.
    After every iteration, we will get the next maximum number.
    """
    for i in range(len(array)):
        isSwapped=False
        for j in range(1,len(array)-i):
            if array[j-1]>array[j]:
                array[j],array[j-1]=array[j-1],array[j] #swapped
                isSwapped=True
        if isSwapped==False:
            return array
    return array

def BubbleSortRecursive(array,iteration,position):
    """
    At every iteration, we will compare only the first (iteration-1) elements with it's next element,
    and if it's greater than the next element, then swap and finally decrease iteration by 1.
    Repeat this step, till iteration is zero.
    """
    if iteration==0:
        return array
    if position<iteration:
        if array[position]>array[position+1]:
            array[position],array[position+1]=array[position+1],array[position]
        return BubbleSortRecursive(array,iteration,position+1)
    else:
        return BubbleSortRecursive(array,iteration-1,0)



arr=[-5,5,-4,4,-3,3,-2,2,-1,1,0]
print(BubbleSort(arr))
print(BubbleSortRecursive(arr,len(arr)-1,0))