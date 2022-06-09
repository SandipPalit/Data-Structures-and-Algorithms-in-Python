def SubsetGeneration(array):
    """
    We will iterate from 0 to 2^(len(array)-1) and get the possible combinations.
    For each number, we will convert it to binary and traverse through the bits.
    If the bit is 1, then take the number at the same index from the array and form a temporary array.
    Append all the temporary array.
    PS: This will work for small size of array (<=15)
    """
    size=len(array)
    allSubsets=[]
    for subsetMask in range(1<<size):
        subset=[]
        for i in range(size):
            if subsetMask & (1<<i) !=0:
                subset.append(array[i])
        if subset not in allSubsets:
            allSubsets.append(subset)
    return allSubsets


print(SubsetGeneration([1,2,2]))