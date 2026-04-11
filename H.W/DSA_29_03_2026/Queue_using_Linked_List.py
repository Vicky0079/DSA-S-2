class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return
        
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return
        
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("NULL")


# MAIN
print("Queue:")
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()