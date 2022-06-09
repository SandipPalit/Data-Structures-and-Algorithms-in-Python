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

def getNode(head,index):                                                    # get the node at the specific index
    while index>0:
        head=head.next
        index-=1
    return head

def BubbleSort(head,iteration,position):
    """
    At every iteration, we will compare only the first (iteration-1) elements with it's next element,
    and if it's greater than the next element, then swap and finally decrease iteration by 1.
    Repeat this step, till iteration is zero.
    """
    if iteration==0 or head==None:
        return head
    if position < iteration:
        node1=getNode(head,position)
        node2=getNode(head,position+1)
        if node1.value>node2.value:
            if node1==head:
                node1.next=node2.next
                node2.next=node1
                head=node2
            else:
                node0=getNode(head,position-1)
                node1.next=node2.next
                node0.next=node2
                node2.next=node1
        # print("Step: ",end="")
        # display(head)
        return BubbleSort(head,iteration,position+1)
    else:
        return BubbleSort(head,iteration-1,0)



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
    display(BubbleSort(sp.head,sp.size-1,0))