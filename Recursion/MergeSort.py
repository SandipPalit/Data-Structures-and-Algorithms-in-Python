"""
Initially we will recursively divide the array into two parts, until each part contains only one element.
Then we will merge the sub parts, in a sorted manner.
"""

def MergeSort(array,start,end):
    if (end-start)==1:
        return
    mid=(start+end)//2
    MergeSort(array,start,mid)
    MergeSort(array,mid,end)
    Merge(array,start,mid,end)

def Merge(array,start,mid,end):
    leftPointer=start
    rightPointer=mid
    tempArray=[]
    while(leftPointer<mid and rightPointer<end):
        if array[leftPointer]<array[rightPointer]:
            tempArray.append(array[leftPointer])
            leftPointer+=1
        else:
            tempArray.append(array[rightPointer])
            rightPointer+=1
    while(leftPointer<mid):
            tempArray.append(array[leftPointer])
            leftPointer+=1
    while(rightPointer<end):
            tempArray.append(array[rightPointer])
            rightPointer+=1
    for iter in range(len(tempArray)):
        array[start+iter]=tempArray[iter]

arr=[-5,5,-4,4,-3,3,-2,2,-1,1,0]
MergeSort(arr,0,len(arr))
print(arr)