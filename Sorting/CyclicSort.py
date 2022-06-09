def CyclicSort(array):
    """
    If a sorted array contains numbers from 1 to N, Then every element will be at (element-1) index.
    So, for each element we will check whether this element is at its correct index,
    If Yes, then move to next element.
    If No, then replace the element with its correct index.
    Repeat this last step, untill this this element is equal to (index+1).
    """
    i=0
    while i<len(array):
        correctIndex=array[i]-1
        if 1<=array[i]<=len(array) and array[i]!=array[correctIndex]:
            array[i],array[correctIndex]=array[correctIndex],array[i]
        else:
            i+=1
    return array


arr=[1,5,2,4,3]
print(CyclicSort(arr))