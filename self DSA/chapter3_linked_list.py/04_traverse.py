class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.n = 0
    
    def __len__(self):
         return self.n
    
    def insert_head(self,value):

        #create node
        new_node = Node(value)
        #create connection
        new_node.next = self.head
        #reassign head
        self.head = new_node
        #increment in n
        self.n = self.n + 1
    def traverse(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
L = Linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.traverse()
        