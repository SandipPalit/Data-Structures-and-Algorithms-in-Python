def QuickSort(array, start,end):
    """
    We are taking the middle element as the pivot and shifting all the greater elements to right side
    and all the smaller elements to left side. So pivot is now at correct position.
    Recursively repeat the step for left and right subpart.
    """
    if start>=end:
        return
    leftPointer=start
    rightPointer=end
    pivot=array[(leftPointer+rightPointer)//2]
    while leftPointer<=rightPointer:
        while array[leftPointer]<pivot:
            leftPointer+=1
        while array[rightPointer]>pivot:
            rightPointer-=1
        if leftPointer<=rightPointer:
            array[leftPointer],array[rightPointer]=array[rightPointer],array[leftPointer]
            leftPointer+=1
            rightPointer-=1
    QuickSort(array,start,rightPointer)
    QuickSort(array,leftPointer,end)

arr=[-5,5,-4,4,-3,3,-2,2,-1,1,0]
QuickSort(arr,0,len(arr)-1)
print(arr)