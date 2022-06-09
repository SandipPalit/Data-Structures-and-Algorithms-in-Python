def StringsCombination(combinations,processed,unprocessed,processedPos,unprocessedPos):
    """
    At every recursion, we are appending [processed[processedPos]+unprocessed[unprocessedPos]
    to the combinations list. Then we are incrementing value of processedPos and unprocessedPos.
    """
    if processedPos==len(processed):
        return StringsCombination(combinations,processed,unprocessed,0,unprocessedPos+1)
    if unprocessedPos==len(unprocessed):
        return combinations
    return StringsCombination(combinations+[processed[processedPos]+unprocessed[unprocessedPos]],processed,unprocessed,processedPos+1,unprocessedPos)

print(StringsCombination([],"ABC","123",0,0))