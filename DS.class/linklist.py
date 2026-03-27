# Node class
class Node:
    def __init__(self, data):
        self.data = data  # store value
        self.next = None  # pointer to next nodep

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # initially empty list

    # 1. Traverse and display
    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")

    # 2. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 3. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node    

    # 4. Delete a node by value
    def delete_node(self, key):
        current = self.head

        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:  # key not found
            print(f"{key} not found in the list")
            return

        prev.next = current.next
        current = None

# Example usage
llist = SinglyLinkedList()

# Insert elements
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_beginning(5)
llist.insert_at_end(30)

# Traverse
print("Linked List:")
llist.traverse()  # Output: 5 -> 10 -> 20 -> 30 -> NULL

# Delete element
llist.delete_node(20)
print("After deleting 20:")
llist.traverse()  # Output: 5 -> 10 -> 30 -> NULL
