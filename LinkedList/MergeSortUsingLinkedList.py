class Node:                                                                 # structure of each Node
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

def getMid(head):                                                           # get the middle node of a linked list
    """
    We will use the fast and slow pointer method, to calculate the middle node of the linked list.
    The fast pointer traverses two nodes at a time and the slow pointer traverses one node at a time.
    So when the fast pointer will reach the tail, the slow pointer will reach to the middle node.
    """
    fast=head
    slow=head
    if fast and fast.next:
        fast=fast.next.next                                                 # one extra traversal for fast pointer, since we need the previous node of the middle node.
    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    midNode=slow.next
    slow.next=None
    # print("Left Part:  ",end="")
    # display(head)
    # print("Right Part:  ",end="")
    # display(midNode)
    return midNode

def merge(head1,head2):                                                     # Merge two Linked List
    """
    We will merge both the lists in ascending order, in a new linked list.
    We will compare the head of both the list and will append the smaller one to the output list.
    If one list is completely traversed, then we will append the rest of the elements from the another list to the output list.
    """
    head=Node()
    temp=head
    while head1 and head2:
        if head1.value < head2.value:
            temp.next=Node(head1.value)
            temp=temp.next
            head1=head1.next
        else:
            temp.next=Node(head2.value)
            temp=temp.next
            head2=head2.next
    while head1:
        temp.next=Node(head1.value)
        temp=temp.next
        head1=head1.next
    while head2:
        temp.next=Node(head2.value)
        temp=temp.next
        head2=head2.next
    # print("Merged:  ",end="")
    # display(head.next)
    return head.next

def MergeSort(head):                                                        # Merge Sort on Linked List
    """
    If there is no or one node is present, then it's already sorted.
    We will find the mid node.
    Then we will recursively sort the Head to (Mid-1) nodes and Mid to Tail nodes.
    Finally we will merge both of these sub-parts in ascending order.
    """
    # print("\nMerge Sort:  ",end="")
    # display(head)
    if head==None or head.next==None:
        return head
    mid=getMid(head)
    left=MergeSort(head)
    right=MergeSort(mid)
    return merge(left,right)


if __name__=="__main__":
    sp=SingularLinkedList()
    sp.insertAtLast(1)
    sp.insertAtLast(9)
    sp.insertAtLast(2)
    sp.insertAtLast(8)
    sp.insertAtLast(3)
    sp.insertAtLast(7)
    sp.insertAtLast(4)
    sp.insertAtLast(6)
    sp.insertAtLast(5)
    sp.insertAtLast(1)
    print("Before Sorting:  ",end="")
    display(sp.head)
    print("After Sorting:   ",end="")
    display(MergeSort(sp.head))