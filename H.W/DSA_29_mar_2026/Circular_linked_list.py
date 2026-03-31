class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Display list
    def display(self):
        if self.head is None:
            return
        
        temp = self.head
        while True:
            print(temp.data, end=" → ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


cll = CircularLinkedList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)

cll.display()