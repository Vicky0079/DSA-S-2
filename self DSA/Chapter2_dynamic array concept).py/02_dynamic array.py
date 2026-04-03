import ctypes
class Meralist:
    def __init__(self):
        self.size = 1
        self.n = 0

# create a c type array with size = self.size
        self.A = self.__make_array(self.size)
    
    def __len__(self):
        return self.n   
    #print
    def __str__(self):
        #[1,2,3]
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
        
    def append(self,item):
        if self.n == self.size:
            #resize 
            self.__resize(self.size*2)
        
     #append
        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return 'Empty list'
        print(self.A[self.n-1])    
        self.n = self.n-1

    def clear(self):
        self.n = 0
        self.size = 1
    
    def find(self,item):

       for i in range(self.n):
           if self.A[i] == item:
               return i
       return 'ValueError - not in list' 


    def __resize(self,new_capacity):
        #create a new array with size = new_capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        #reassign A
        self.A = B


    
    def __make_array(self,capacity):
        #create a c type array(static,referntial) with size capacity
        return (capacity * ctypes.py_object)()
L  = Meralist()
print(L)
print(len(L))
L.append('hello')
L.append(3.4)
L.append(True)
L.append(100)
print(len(L))
print(L)
print(L[2])
print(L[30])
L.pop()
print(L)
# L.clear()
# print(L)
print(L.find('hello'))
print(L.find('helloo'))
