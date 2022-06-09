class Node:                                                     # structure of each Node
    def __init__(self,value=None):
        self.value=value
        self.next=None


class SingularLinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def insert(self,value,position,presentNode):                # insert at any position
        if position<0 or position>self.size:
            print("Cannot Insert")
            return
        if presentNode==None:
            if self.size==0:
                self.head=Node(value)
                self.size+=1
                return
            return
        if position==0:                                         # insert at first
            tempNode=Node(value)
            tempNode.next=self.head
            self.head=tempNode
            self.size+=1
            return
        if position==1:                                         # insert at any other position
            tempNode=Node(value)
            tempNode.next=presentNode.next
            presentNode.next=tempNode
            self.size+=1
            return
        return self.insert(value,position-1,presentNode.next)

    def delete(self,position,presentNode):                      # delete from any position
        if position<0 or position>=self.size:
            print("Cannot Delete")
            return
        if presentNode==None:
            return
        if position==0:                                         # delete from first
            self.head=self.head.next
            self.size-=1
            return
        if position==1:                                         # delete from any other position
            if presentNode.next:
                presentNode.next=presentNode.next.next
            self.size-=1
            return
        return self.delete(position-1,presentNode.next)



    def __str__(self):
        printString=""
        if self.head==None:
            return "None"
        tempNode=self.head
        while tempNode.next is not None:
            printString+=str(tempNode.value)+" --> "
            tempNode=tempNode.next
        printString+=str(tempNode.value)
        printString+=" --> None"
        return printString


if __name__=="__main__":
    sp=SingularLinkedList()
    print(sp)
    sp.insert(1,0,sp.head)                                      # insertAtFirst
    print(sp)
    sp.insert(0,0,sp.head)
    print(sp)
    sp.insert(5,sp.size,sp.head)                                # insertAtLast
    print(sp)
    sp.insert(3,2,sp.head)                                      # insertAtPos
    print(sp)
    sp.insert(4,3,sp.head)
    print(sp)
    sp.insert(4,9,sp.head)
    print(sp)
    sp.delete(9,sp.head)
    print(sp)
    sp.delete(0,sp.head)                                        # deleteFromFirst
    print(sp)
    sp.delete(sp.size-1,sp.head)                                # deleteFromLast
    print(sp)
    sp.delete(1,sp.head)                                        # deleteFromPos
    print(sp)
    sp.delete(1,sp.head)
    print(sp)
    sp.delete(0,sp.head)
    print(sp)