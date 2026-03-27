class StackADT:
 def __init__(self):
    self.data = []

 def push(self, x):
    self.data.append(x)

 def pop(self):
   self.data = []  

 def push(self, x):
   self.data.append(x)

 def pop(self):
    if self.is_empty():
       return None
    return self.data.pop()

 def peek(self):
   if self.is_empty():
     return None
   return self.data[-1]
 
def is_empty(self):
   return len(self.data) == 0

def size(self):
  return len(self.data)

def display(self):
   return self.data


def reverse_string_using_stack(s):
  st = StackADT()
  for ch in s:
   st.push(ch)
  rev = ""