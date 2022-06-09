##Observations

* Recursion is a Function calling itself.
* Space complexity won't be constant, due to the stack.
* When stack is full, Stack Overflow error occurs.

###Josephus Problem
* Initially we will create an array containing 0 to (N-1). We will calculate the next position using the formula (lastPos+jump)%len(array) and remove that element from the array. We will repeat this step until only one element is remaining. Return that element.

###Merge Sort
* Recursively divides the array till it contains only one element.
* Then merges the subparts in a sorted manner.
* Best case time: N * Log N.
* Worst case time: N * Log N.
* Not a in-place sort.
* Recommended for Linked Lists, as unlike arrays linked lists doesn't occupy continuous block of memory.

###Quick Sort
* Moves greater element to right side and smaller elements to left side of pivot.

###String Permutation
* For N characters, N! permutations will be formed.
* At every level, first character of unprocessed is inserted into all possible combinations in processed.

###Strings Combination
* For two strings with N and M characters respectively, N*M combinations will be formed.
