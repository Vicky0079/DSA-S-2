class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        
        self.head = new_node

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
        print("NULL")


dll = DoublyLinkedList()
dll.insert_begin(30)
dll.insert_begin(20)
dll.insert_begin(10)

dll.display()