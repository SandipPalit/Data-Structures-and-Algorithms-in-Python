## Observations

* What my array would look like, If I had not taken this path.
* While returning from the function, revert the changes that were made whaile calling the function.

### N Queen
* Queens can attack in horizontal, vertical and diagonal direction.
* Time Complexity: O(N!)

### N Knight
* Knight can attack in UUR, RRU, RRD, DDR, DDL, LLD, LLU & UUL  (U=Up, R=Right, D=Down & L=Left).
* In “deepcopy()” function,  any changes made to a copy of object do not reflect in the original object. In “copy()” function, any changes made to a copy of object do reflect in the original object.

### Sudoku Solver
* At each empty cell, we will place a number from 1 to 9 and recursively repeat this step. If it cannot solve the sudoku, then we will backtrack and try with another number.
* Time Complexity: 9<sup>N<sup>2</sup></sup>
