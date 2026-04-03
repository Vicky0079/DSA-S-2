class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linkedlist:

    def __init__(self):
        # Empty Linkedlist List
        self.head = None
        # no of nodes in the LL
        self.n = 0
    
    def __len__(self):
        return self.n
    
L = Linkedlist()
print(L)
print(len(L))
