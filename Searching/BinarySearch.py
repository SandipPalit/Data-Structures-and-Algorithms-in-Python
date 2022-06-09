"""
This is order agnostic binary search, where we know that the array is sorted but we don't know in which order it is sorted.
"""


def BinarySearchIterative(left,right,array,target):
    if array[left]<array[right]:        # Ascending Order
        isAscending=True
    elif array[left]>array[right]:      # Descending Order
        isAscending=False
    else:                               # Array contains only one unique element
        if array[left]==target:
            return left
        else:
            return -1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        if target>array[mid]:
            if isAscending:
                left=mid+1
            else:
                right=mid-1
        else:
            if isAscending:
                right=mid-1
            else:
                left=mid+1
    return -1


def BinarySearchRecursive(left,right,array,target):
    mid=(left+right)//2
    if left>right and array[mid]!=target: # target not found
        return -1
    if array[mid]==target:
        return mid
    if array[left]<array[right]:        # Ascending Order
        isAscending=True
    else:                               # Descending Order
        isAscending=False
    if target>array[mid]:
        if isAscending:
            return BinarySearchRecursive(mid+1,right,array,target)
        else:
            return BinarySearchRecursive(left,mid-1,array,target)
    else:
        if isAscending:
            return BinarySearchRecursive(left,mid-1,array,target)
        else:
            return BinarySearchRecursive(mid+1,right,array,target)


arr1=[0,1,4,7,9,10,12]
arr2=[99,78,67,56,45,34,23,12]

print(BinarySearchIterative(0,len(arr1)-1,arr1,10))
print(BinarySearchIterative(0,len(arr2)-1,arr2,67))

print(BinarySearchRecursive(0,len(arr1)-1,arr1,10))
print(BinarySearchRecursive(0,len(arr2)-1,arr2,67))