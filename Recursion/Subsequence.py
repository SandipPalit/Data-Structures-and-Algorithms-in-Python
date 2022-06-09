def Subsequence(processed, unprocessed):
    """
    At every recursive step, we are making two recursive calls, we are taking the first character of the
    unprocessed in one call and we are rejecting it in the another call.
    """
    if len(unprocessed)==0:
        return [processed]
    notTaking=Subsequence(processed,unprocessed[1:])
    taking=Subsequence(processed+unprocessed[0],unprocessed[1:])
    return notTaking+taking

print(Subsequence("","ABC"))