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
        #create new node 
        new_node = Node(value)
        #create connection
        new_node.next = self.head
        #reassign head
        self.head = new_node
        #increment in n
        self.n = self.n + 1
    
    def traverse(self):
        #create current node to 1 node
        curr = self.head
        #then run it to end whic is till none
        while curr != None:
            print(curr.data)
        #for print next node data
            curr = curr.next
    
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            #empty
            self.head = new_node
            self.n = self.n + 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        #you are at the last node
        curr.next = new_node
        self.n = self.n + 1

L = Linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
# L.traverse()
L.append(5)
L.traverse()

