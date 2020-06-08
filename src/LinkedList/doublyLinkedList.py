class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class LinkedList:
    def __init__(self):
        self.head = None

    def addAtStart(self,data):
        node = Node(data, self.head, None)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def printForward(self):
        if self.head is None:
            print "list is Empty"
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print llstr

    def printBackward(self):
        if self.head is None:
            print "List is Empty"
            return
        lastNode = self.getLastNode()
        itr = lastNode
        llstr = ''
        while itr:
            llstr+= str(itr.data) + '-->'
            itr = itr.prev
        print "link list in reserve: ",llstr

    def getLength(self):
        count = 0
        itr = self.head
        while itr.next:
            count+=1
            itr = itr.next
        return count

    def insertAtIndex(self,index,data):
        if index<0 or index>self.getLength():
            raise Exception("Invalid Entry")
        if index==0:
            self.addAtStart(data)
        itr = self.head
        count = 0
        while itr:
            if count==index-1:
                node = Node(data,itr.next,itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count+=1
    def getLastNode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def removeAtIndex(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid Index")
        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count+=1
    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.addAtStart(2)
    ll.addAtStart(3)
    ll.addAtStart(24)
    ll.printForward()
    ll.insertAtIndex(0,110)
    ll.printForward()
    ll.removeAtIndex(2)
    ll.printForward()
    ll.insertValues(["jack",1,1.2])
    ll.printForward()

