## Observations

### Singular Linked List
* The Node contains Value and Next (a link to next node).
* We can only look at the next node and there is no option to look at the previous node.
* Linked List traversal takes O(N) time.
* We can even optimize the Linked List by using a tail variable.

### Doubly Linked List
* The Node contains Value, Next (a link to next node) and Prenious (a link to previous node).
* We can look at both next node and previous node.

### Circular Linked List
* The Node contains Value and Next (a link to next node).
* We can only look at the next node and there is no option to look at the previous node.
* The Next of Tail will point to Head.
* Insert or delete from first is exactly same as insert or delete from last.

### Inbuilt implementation
* Python has Deque library, which functions much like a doubly linked list.
* Deque also has the functionality of stack (LIFO) and queue (FIFO).

### Singular Linked List using Recursion
* To modify a node, we should traverse to its previous node.
* A single insert or delete operation is enough to perform all the insert or delete operations resp.

### Fast And Slow Pointer
* Here we will take two pointers, one pointer will be slow (traverse 1 node at a time) and another pointer will be fast (traverse 2 node at a time).
* The logic behind this cycle detection is, if in a circular track two person run at different speed, then the person who is running fast will overtake the person who is running slow at some point.

### Merge Sort
* Recursively divides the array till it contains only one element.
* Then merges the sub-parts in a sorted manner.
* Here we are passing the head node in every function, not the entire linked list.

### Bubble sort
* After every iteration, we get the next maximum or minimum.
* The order of duplicate elements are maintained.
* Here we are passing the head node in every function, not the entire linked list.

### Reversal of Linked List
* In the in-place reversal of Linked List, we used the 3 pointer method.
* We can also perform this using Recursion, but the recursion-stack will take some extra space.
