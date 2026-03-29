
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new = Node(data)
        if not self.rear:
            self.front = self.rear = new
            return
        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if not self.front:
            return "Empty"
        val = self.front.data
        self.front = self.front.next

        if self.front is None:   
            self.rear = None

        return val

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" <- ")
            temp = temp.next
        print("None")


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue:")
q.display()

print("Dequeue:", q.dequeue())

print("After Dequeue:")
q.display()