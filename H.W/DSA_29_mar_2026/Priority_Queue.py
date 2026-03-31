class PriorityNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, data, priority):
        new_node = PriorityNode(data, priority)

        if self.head is None or self.head.priority > priority:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            
            new_node.next = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.data}({temp.priority})", end=" → ")
            temp = temp.next
        print("NULL")


# MAIN
print("Priority Queue:")
pq = PriorityQueue()
pq.insert("A", 2)
pq.insert("B", 1)
pq.insert("C", 3)
pq.display()