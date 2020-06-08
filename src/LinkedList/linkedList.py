class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addAtBegining(self,data):
        self.head = Node(data,self.head)

    def printList(self):
        if self.head is None:
            print "List is Empty"
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print llstr

    def addAtEnd(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next =  Node(data,None)

    def getLength(self):
        count = 0
        if self.head is None:
            return 0
        itr = self.head
        while itr.next:
            itr = itr.next
            count+=1
        print count
        return count
    def addAtIndex(self,index, data):
        if index<0 or index>self.getLength():
            raise Exception("Invalid Index")

        if index==0:
            self.addAtBegining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def removeAtIndex(self,index):
        if index<0 or index>self.getLength():
            raise Exception("Invalid Index")
        count = 0

        itr = self.head
        if index==0:
            self.head = itr.next
            return
        while itr.next:
            if count==index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.addAtEnd(data)

    def removeByValue(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insertAfterValue(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next


if __name__== '__main__':
    ll = LinkedList()
    ll.addAtEnd(10)
    ll.printList()
    ll.addAtBegining(2)
    ll.addAtBegining(6)
    ll.addAtBegining(9)
    ll.printList()
    ll.getLength()
    ll.addAtIndex(1,4)
    ll.printList()
    ll.removeAtIndex(4)
    ll.printList()
    ll.insertValues([5,6,7,8,9])
    ll.removeByValue(9)
    ll.printList()
    ll.insertAfterValue(8,9)
    ll.printList()

