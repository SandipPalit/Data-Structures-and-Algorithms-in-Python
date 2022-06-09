class Node:                                                             # structure of each Node
    def __init__(self,value=None):
        self.value=value
        self.previous=None
        self.next=None


class DoublyLinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0

    def insertAtFirst(self,value):
        newNode=Node(value)
        if self.__size==0:
            self.__head=newNode
            self.__tail=newNode
            self.__size+=1
            return
        newNode.next=self.__head
        self.__head.previous=newNode
        self.__head=newNode
        self.__size+=1

    def insertAtLast(self,value):
        if self.__size==0:
            self.insertAtFirst(value)
            return
        newNode=Node(value)
        self.__tail.next=newNode
        newNode.previous=self.__tail
        self.__tail=newNode
        self.__size+=1

    def insertAtPos(self,value,position):
        if position<1 or position>self.__size:
            print("Position out of bound")
            return
        if position==1:
            self.insertAtFirst(value)
            return
        if position==self.__size:
            self.insertAtLast(value)
            return
        newNode=Node(value)
        tempNode=self.__head
        while position>2:
            position-=1
            tempNode=tempNode.next
        newNode.next=tempNode.next
        newNode.next.previous=newNode
        newNode.previous=tempNode
        tempNode.next=newNode
        self.__size+=1

    def positionOf(self,value):
        tempNode=self.__head
        pos=0
        while tempNode is not None:
            pos+=1
            if tempNode.value==value:
                return pos
            tempNode=tempNode.next
        return -1

    def deleteFromFirst(self):
        if self.__head==None:
            return "Cannot delete"
        if self.__size==1:
            returnedValue=self.__head.value
            self.__head=None
            self.__tail=None
            self.__size-=1
            return returnedValue
        returnedValue=self.__head.value
        self.__head=self.__head.next
        self.__head.previous=None
        self.__size-=1
        return returnedValue

    def deleteFromLast(self):
        if self.__head==None:
            return "Cannot delete"
        if self.__size==1:
            returnedValue=self.__head.value
            self.__head=None
            self.__tail=None
            self.__size-=1
            return returnedValue
        returnedValue=self.__tail.value
        self.__tail=self.__tail.previous
        self.__tail.next=None
        self.__size-=1
        return returnedValue

    def deleteFromPos(self,position):
        if self.__head==None:
            return "Cannot delete"
        if self.__size==1:
            returnedValue=self.__head.value
            self.__head=None
            self.__tail=None
            self.__size-=1
            return returnedValue
        if position<1 or position>self.__size:
            return "Position out of bound"
        if position==1:
            return self.deleteFromFirst()
        if position==self.__size:
            return self.deleteFromLast()
        tempNode=self.__head
        while position>2:
            position-=1
            tempNode=tempNode.next
        returnedValue=tempNode.next.value
        tempNode2=tempNode.next.next
        tempNode2.previous=tempNode
        tempNode.next=tempNode2
        self.__size-=1
        return returnedValue

    def __str__(self):
        printString="None <-- "
        if self.__head==None:
            return "None"
        tempNode=self.__head
        while tempNode.next is not None:
            printString+=str(tempNode.value)+" <==> "
            tempNode=tempNode.next
        printString+=str(tempNode.value)
        printString+=" --> None"
        return printString

    def __len__(self):
        return self.__size


if __name__=="__main__":
    sp=DoublyLinkedList()
    print(sp)
    sp.insertAtFirst(4)
    print(sp)
    sp.insertAtFirst(5)
    print(sp)
    sp.insertAtLast(2)
    print(sp)
    sp.insertAtLast(1)
    print(sp)
    print("Position:  ",sp.positionOf(2))
    print(sp)
    sp.insertAtPos(3,3)                                                     # 1-indexed
    print(sp)
    print("Deleted:  ",sp.deleteFromFirst())
    print(sp)
    print("Deleted:  ",sp.deleteFromLast())
    print(sp)
    print("Deleted:  ",sp.deleteFromPos(2))
    print(sp)
    print("Deleted:  ",sp.deleteFromPos(1))
    print(sp)
    print("Deleted:  ",sp.deleteFromPos(1))
    print(sp)