class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    # Insert at end
    def insert_end(self, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    # Delete at beginning
    def delete_begin(self):
        if self.head:
            self.head = self.head.next

    # Delete at end
    def delete_end(self):
        temp = self.head
        if temp is None:
            return

        if temp.next is None:
            self.head = None
            return

        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Delete by value
    def delete_value(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        while temp.next and temp.next.data != x:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next

    # Traverse
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Test Linked List
ll = LinkedList()
ll.insert_begin(10)
ll.insert_begin(5)
ll.insert_end(20)
ll.insert_end(30)

print("Linked List:")
ll.traverse()