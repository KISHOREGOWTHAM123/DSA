"""
    Singly Linked list data structure
"""

class Node:
    
    def __init__(self, value = None, next = None) -> None:
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def append(self, value: int) -> None:
        if not self.head:
            self.head = Node(value)
            self.length += 1
            return
        
        temp: Node = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(value)
        self.length += 1
    
    def prepend(self, value: int) -> None:
        if not self.head:
            self.head = Node(value)
            self.length += 1
            return
        self.head = Node(value, next=self.head)
        self.length += 1
    
    def insert(self, index: int, value: int) -> None:
        if index < 0 or index > self.length:
            raise "index out of range"
        if not self.head:
            self.head = Node(value)
            self.length += 1
            return
        if not index:
            self.prepend(value)
            return
        if index == self.length - 1:
            self.append(value)
            return
        temp: Node = self.head
        count: int = 0
        while count < index - 1:
            temp = temp.next
            count += 1
        temp.next = Node(value, next=temp.next)
        self.length += 1

    def pop(self, index = None) -> None:
        if not self.head:
            raise "linked list is empty"
        if index and (index < 0 or index > self.length):
            raise "index out of range"
        if self.length == 1:
            temp = self.head
            self.head = None
            self.length -= 1 
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        if not index:
            temp: Node = self.head
            while temp.next != None:
                prev = temp
                temp = temp.next
            prev.next = None
            self.length -= 1
            return
        count: int = 0
        temp: Node = self.head
        while count < index - 1:
            temp = temp.next
            count += 1
        temp.next = temp.next.next
        self.length -= 1
        
    def traverse(self) -> None:
        temp: Node = self.head
        print("HEAD -> ", end='')
        while temp.next != None:
            print(temp.value, end =" -> ")
            temp = temp.next
        print(temp.value)


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.prepend(4)
l.insert(0, 10)
l.insert(4, 20)
l.insert(1, 30)
l.insert(5, 40)
l.pop()
l.pop(0)
l.pop(5)
l.pop(2)
print(l.length)
l.traverse() # HEAD -> 30 -> 4 -> 2 -> 40