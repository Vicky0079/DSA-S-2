
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return "Empty"
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return "Empty"
        return self.head.data

st = Stack()
st.push(10)
st.push(20)
st.push(30)

print("Top:", st.peek())
print("Pop:", st.pop())
print("Top:", st.peek())