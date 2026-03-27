class maths:
   def __init__(self):
      self.menu()

   def menu(self):
      user_input = int(input("""
      I can help u for add and subtract
      1.choose 1 for add
      2.choose 2 for subtract
        """))
   
      if user_input == 1:
         print(self.add())
         self.menu()
      
      if user_input == 2:
         print(self.subtract())
         self.menu()
      else:
         exit()
    
   def add(self):
      a = int(input("Enter your 1st no"))
      b = int(input("Enter your 2nd no."))
      return a+b 
      
      
   def subtract(self):
      a = int(input("Enter your 1st no"))
      b = int(input("Enter your 2nd no."))
      return a-b
    
      
m = maths()


   

  
      
   