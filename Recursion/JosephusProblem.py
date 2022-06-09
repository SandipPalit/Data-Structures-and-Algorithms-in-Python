def FindJosephus(array,lastPos,jump):
    if len(array)==1:
        # Josephus found
        return array[0]
    nextPos=(lastPos+jump)%len(array)
    array.pop(nextPos)
    return FindJosephus(array,nextPos,jump)

def JosephusProblem(N,K):
    """
    Josephus Problem:
    There are N people standing in a circular line. 1st person will start counting in clockwise direction
    (including himself) and will kill the K-th person, then the (K+1) will repeat the same thing and
    this will go on, until only one person is left. Who will be that person?

    Solution:
    Initially we will create an array containing 0 to (N-1). We will calculate the next position using the formula
    (lastPos+jump)%len(array) and remove that element from the array. We will repeat this step until only one
    element is remaining. Return that element.
    """
    peoples=[i for i in range(N)]
    return FindJosephus(peoples,0,K-1)

print(JosephusProblem(5,2))