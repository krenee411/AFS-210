from random import randint


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self):
        return self.count

    def first(self):
        return self.head

    def last(self):
        return self.tail


    def addFirst(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.count += 1
       

    def addLast(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
            node.prev = temp
        self.count += 1


    def addAtIndex(self, data, index):
        node = Node(data)
        if index < 0:
            print("you have entered an index that is out of range.")
        elif index == 0:
            self.next = self.head
            self.head.prev = node
            self.head = node
            self.count += 1
        else:
            temp = self.head
            for i in range(1, index-1):
                if temp != None:
                    temp = temp.next
            if temp != None:
                node.next = temp.next
                node.prev = temp
                temp.next = node
                self.count += 1
            else: 
                print("The index give is out of range")

    def indexOf(self, data):   
        temp = self.head
        found = 0
        index = -1
        if temp != None:
            while temp != None:
                index +=1 
                if temp.data == data:
                    found += 1 
                    break
                temp = temp.next
            if found == 1:
                print(index)
            else:
                print("Item not found")
        else:
            print("The list is currenly empty")
            


    def add(self, data) -> None:
        self.addLast(data)

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

    def shuffle(self):
        if self.head == None:
            return
        else:
            current = self.head
            while current.next != None:
                index= current.next
                while index != None:
                    if (randint(0,1) == 1):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next