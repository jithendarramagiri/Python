class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        # LL not empty
        new_node.next = self.head
        self.head.prev =new_node
        self.head = new_node

    def insert_at_ending(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        # LL not empty
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_at_position(self,position,data):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.insert_at_beginning(data)
            return
        # if position is gretater than 0
        new_node = Node(data)
        current = self.head
        for _ in range(position):
            current = current.next
        previous_node = current.prev
        new_node.prev = previous_node
        new_node.next = current
        previous_node.next = new_node
        current.prev = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        # LL has more than One element
        self.head = self.head.next
        self.head.prev = None

    def delete_at_ending(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        # LL has more than one element
        self.tail = self.tail.prev
        self.tail.next = None

    def delete_at_position(self,position):
        current = self.head
        for _ in range(position):
            current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev

    def length(self):
        count = 0
        current = self.head
        while current is not None :
            count += 1
            current = current.next
        return(count)

    def display_forward(self):
        current = self.head
        while current is not None:
           print(current.data, end= "<->")
           current = current.next
        print(None)


    def display_backward(self):
        current = self.tail
        while current is not None:
            print(current.data, end="<->")
            current = current.prev

        print(None)
dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(5)
dll.insert_at_ending(20)
dll.insert_at_ending(25)
dll.insert_at_ending(30)
dll.insert_at_position(2,15)
dll.display_forward()
dll.display_backward()