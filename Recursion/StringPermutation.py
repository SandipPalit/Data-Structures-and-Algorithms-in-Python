def StringPermutation(unprocessed,processed):
    """
    At every level, we are taking the first character of the unprocessed string and inserting it
    into all the possible positions in processed string.
    """
    if len(unprocessed)==0:
        return [processed]
    tempList=[]
    characterToInsert=unprocessed[0]
    for i in range(len(processed)+1):
        leftpart=processed[:i]
        rightPart=processed[i:]
        remainingUnprocessed=unprocessed[1:]
        tempList+= StringPermutation(remainingUnprocessed,leftpart+characterToInsert+rightPart)
    return tempList

print(StringPermutation("ABC",""))