class Node:                                                             # structure of each Node
    def __init__(self,value=None):
        self.value=value
        self.next=None


class SingularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insertAtLast(self,value):
        newNode=Node(value)
        if self.size==0:
            newNode.next=self.head
            self.head=newNode
            self.tail=newNode
            self.size+=1
            return
        self.tail.next=newNode
        self.tail=newNode
        self.size+=1

    def display(self,nodeToPrint):
        printString=""
        if self.head==None:
            return "None"
        tempNode=self.head
        while nodeToPrint>0:
            printString+=str(tempNode.value)+" --> "
            tempNode=tempNode.next
            nodeToPrint-=1
        printString+=str(tempNode.value)
        print(printString)


def detectCycle(head):
    """
    We will take two pointers: Slow and Fast. The slow pointer will move by one node and
    the fast pointer is moving by two nodes.
    If the fast pointer reaches Null, then no cycle is present. But if fast pointer meets
    slow pointer at any node, then cycle is present and both of the pointers are within the cycle.
    As if there is any cycle present, then only the fast pointer will overtake the slow pointer.
    """
    slow=head
    fast=head
    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

def lengthOfCycle(head):
    """
    After detecting the cycle, we will start another pointer from that point.
    The next time when that pointer will meet  the fast pointer, one cycle will be completed.
    We will return it's length.
    """
    slow=head
    fast=head
    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:                                                  # cycle found
            length = 1
            temp=slow.next
            while temp!=fast:
                temp=temp.next
                length+=1
            return length
    return 0

def startOfCycle(head):
    """
    After we get the length of the cycle, we will start a pointer from head and traverse exactly 'length' number of nodes.
    Then we will start another pointer from the head and will move both pointers together,
    both of these pointers will meet at the starting of the cycle.
    """
    slow=head
    fast=head
    length=0
    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:                                                  # cycle found
            temp=slow.next
            length+=1
            while temp!=fast:                                           # length calculated
                temp=temp.next
                length+=1
            break
    if length==0:
        return None
    first=head
    while length>0:                                                     # traversed the first pointer 'length' times.
        first=first.next
        length-=1
    second=head
    while first!=second:                                                # traversed both the pointer simultaneously.
        first=first.next
        second=second.next
    return second.value

ll=SingularLinkedList()
ll.insertAtLast(1)
ll.insertAtLast(2)
ll.insertAtLast(3)
ll.insertAtLast(4)
ll.insertAtLast(5)
ll.insertAtLast(6)
ll.insertAtLast(7)
ll.insertAtLast(8)
ll.insertAtLast(9)
ll.tail.next=ll.head.next.next.next                                     # forming the cycle
ll.display(15)
print("Detect Cycle: ",detectCycle(ll.head))
print("Length Of Cycle: ",lengthOfCycle(ll.head))
print("Start Of Cycle: ",startOfCycle(ll.head))