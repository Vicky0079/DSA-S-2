class DynamicArray:
    def __init__(self):
        self.n = 0             
        self.capacity = 1     
        self.A = [None] * self.capacity

    def append(self, element):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)   

        self.A[self.n] = element
        self.n += 1

    def resize(self, new_cap):
        B = [None] * new_cap
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_cap

    def pop(self):
        if self.n == 0:
            return "Empty"
        val = self.A[self.n - 1]
        self.n -= 1
        return val

    def display(self):
        for i in range(self.n):
            print(self.A[i], end=" ")
        print()



arr = DynamicArray()
arr.append(10)
arr.append(20)
arr.append(30)
arr.display()
print("Pop:", arr.pop())
arr.display()