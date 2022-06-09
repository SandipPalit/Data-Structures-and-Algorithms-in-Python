def InsertionSort(array):
    """
    For each element, the left part of the array will be sorted.
    We will insert the element to the correct position on the left part of the array.
    """
    for i in range(len(array)-1):
        for j in range(i+1,-1,-1):
            if array[j]<array[j-1]:
                array[j],array[j-1]=array[j-1],array[j]
            else:
                break
    return array


arr=[-5,5,-4,4,-3,3,-2,2,-1,1,0]
print(InsertionSort(arr))