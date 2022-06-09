from collections import deque
sp=deque([2,3])                             # deque object (similar to doubly linked list)
print(sp)
sp.append(5)                                # insertAtLast
print(sp)
sp.appendleft(1)                            # insertAtFirst
print(sp)
sp.insert(3,4)                              # insertAtPos  (0-indexed)
print(sp)
print("Position: ",sp.index(3))             # positionOf  (0-indexed)
print(sp)
print("Count: ",sp.count(3))                # count of a particular element in a Linked List
print(sp)
print("Length: ",sp.__len__())              # length of the Linked List
print(sp)
print("Value: ",sp.__getitem__(2))          # valueAt  (0-indexed)
print(sp)
sp.extend([6,7,8,9])                        # merge another Linked List at Last
print(sp)
sp.extendleft([0])                          # merge another Linked List at First
print(sp)
sp.reverse()                                # reverse the Linked List
print(sp)
print("Deleted: ",sp.pop())                 # deleteFromLast
print(sp)
print("Deleted: ",sp.popleft())             # deleteFromFirst
print(sp)
sp.remove(5)                                # deleteValue
print(sp)
sp.clear()                                  # delete the entire Linked List
print(sp)