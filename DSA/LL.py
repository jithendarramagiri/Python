
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        # LL empty
        if self.head is None:
            self.head = new_node
            return

        # LL not empty
        new_node.next = self.head
        self.head = new_node


    def insert_at_ending(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node


    def insert_at_position(self, position, data):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.insert_at_beginning(data)
            return

        # Position is greater than 0
        current = self.head
        for i in range(position - 1):
            if current is None:
                print("Invalid position")
                return
            current = current.next
        if current is None:
            print("Invalid position")
            return

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node


    def delete_at_beginning(self):
        # LL empty
        if self.head is None:
            print("List is empty")
            return

        # LL not empty
        self.head = self.head.next


    def delete_at_ending(self):
        # LL empty
        if self.head is None:
            print("List is empty")
            return

        # LL has only one element
        if self.head.next is None:
            self.head = None
            return

        # LL has more than one element
        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None


    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return

        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.head = self.head.next
            return

        # Position is greater than 0
        current = self.head

        for i in range(position - 1):
            if current.next is None:
                print("Invalid position")
                return
            current = current.next

        if current.next is None:
            print("Invalid position")
            return

        current.next = current.next.next


    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


ll = Linkedlist()

ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_ending(30)
ll.insert_at_position(2,15)

ll.display()

ll.delete_at_beginning()
ll.delete_at_ending()

ll.display()

print(ll.has_cycle())

ll.reverse()
ll.display()
