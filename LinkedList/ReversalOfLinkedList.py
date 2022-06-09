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


def display(head):
    if head==None:
        return "None"
    while head is not None:
        print(head.value,end=" --> ")
        head=head.next
    print("None")

def reverseIterative(head):
    """
    Initially we will take the head as CurrentNode and Null as PreviousNode.
    Then we will traverse the whole linked list and we will modify the links as follows.
    We will save the next of the CurrentNode in NextNode and the we will point CurrentNode.Next to PreviousNode to reverse the list.
    Then we will shift to the right ,i.e, currentNode to previousNode and nextNode to currentNode.
    """
    currentNode=head
    previousNode=None
    while currentNode:
        nextNode=currentNode.next
        currentNode.next=previousNode
        previousNode=currentNode
        currentNode=nextNode
    return previousNode

def reverseRecursive(head):
    """
    If there is only one node or it is the last node of the Linked list, then we will return the node.
    Else we will recursively call the next node, and will store the returned node as newHeadNode.
    While returning from the recursive call, we will modify the links in this way.
    We will save the next of head to nextNode and then we will point the next of nextNode to head to reverse the link.
    Finally, we will point the next of head to null and then we will return thr newHeadNode.
    """
    if head==None or head.next==None:
        return head
    newHeadNode=reverseIterative(head.next)
    nextNode=head.next
    nextNode.next=head
    head.next=None
    return newHeadNode


if __name__=="__main__":
    l1=SingularLinkedList()
    l1.insertAtLast(1)
    l1.insertAtLast(2)
    l1.insertAtLast(3)
    l1.insertAtLast(4)
    l1.insertAtLast(5)
    display(l1.head)
    display(reverseIterative(l1.head))

    l2=SingularLinkedList()
    l2.insertAtLast(5)
    l2.insertAtLast(6)
    l2.insertAtLast(7)
    l2.insertAtLast(8)
    l2.insertAtLast(9)
    display(l2.head)
    display(reverseRecursive(l2.head))
