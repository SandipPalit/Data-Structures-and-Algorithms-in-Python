class Node:                                                             # structure of each Node
    def __init__(self,value=None):
        self.value=value
        self.next=None


class CircularLinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0

    def insertAtLast(self,value):
        newNode=Node(value)
        if self.__size==0:
            newNode.next=newNode
            self.__head=newNode
            self.__tail=newNode
            self.__size+=1
            return
        newNode.next=self.__head
        self.__tail.next=newNode
        self.__tail=newNode
        self.__size+=1

    def insertAfter(self,value,posValue):
        newNode=Node(value)
        if self.__size==0:
            return "Cannot insert"
        if posValue==self.__tail.value:
            self.insertAtLast(value)
            return
        tempNode=self.__head
        while tempNode.next is not self.__head:
            if tempNode.value==posValue:
                newNode.next=tempNode.next
                tempNode.next=newNode
                self.__size+=1
                return
            tempNode=tempNode.next
        return "Value not found"

    def insertBefore(self,value,posValue):
        newNode=Node(value)
        if self.__size==0:
            return "Cannot insert"
        if posValue==self.__head.value:
            self.insertAtLast(value)
            return
        tempNode=self.__head
        while tempNode.next is not self.__head:
            if tempNode.next.value==posValue:
                newNode.next=tempNode.next
                tempNode.next=newNode
                self.__size+=1
                return
            tempNode=tempNode.next
        return "Value not found"

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
        self.__tail.next=self.__head
        self.__size-=1
        return returnedValue

    def deleteValue(self,value):
        if self.__head==None:
            return "Cannot delete"
        if self.__size==1:
            if self.__head.value==value:
                returnedValue=self.__head.value
                self.__head=None
                self.__tail=None
                self.__size-=1
                return returnedValue
            else:
                return "Value not found"
        if value==self.__head.value:
            return self.deleteFromFirst()
        tempNode=self.__head
        while tempNode.next is not self.__head:
            if tempNode.next.value==value:
                returnedValue=tempNode.next.value
                tempNode.next=tempNode.next.next
                if tempNode.next==self.__head:
                    self.__tail=tempNode
                self.__size-=1
                return returnedValue
            tempNode=tempNode.next
        return "Value not found"

    def __str__(self):
        printString="|-> "
        if self.__head==None:
            return "None"
        tempNode=self.__head
        while tempNode.next is not self.__head:
            printString+=str(tempNode.value)+" --> "
            tempNode=tempNode.next
        printString+=str(tempNode.value)
        printString+=" -|"
        return printString

    def __len__(self):
        return self.__size


if __name__=="__main__":
    sp=CircularLinkedList()
    print(sp)
    sp.insertAtLast(1)
    print(sp)
    sp.insertAtLast(3)
    print(sp)
    sp.insertAtLast(5)
    print(sp)
    sp.insertAfter(4,3)
    print(sp)
    sp.insertBefore(2,3)
    print(sp)
    print("Deleted: ",sp.deleteFromFirst())
    print(sp)
    print("Deleted: ",sp.deleteFromFirst())
    print(sp)
    print("Deleted: ",sp.deleteValue(4))
    print(sp)
    print("Deleted: ",sp.deleteValue(5))
    print(sp)
    print("Deleted: ",sp.deleteValue(3))
    print(sp)