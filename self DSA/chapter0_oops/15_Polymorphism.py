#Polymorphism

# 1)Method Overriding
# 2)Method Overloading
# 3)Operator OverLoading

# -----------------------------------------------------------------------------------------------------------------------------------
# 1)Method overriding

# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera
    
    
# class SmartPhone(Phone):
#     def __init__(self, os, ram):
#         self.os = os
#         self.ram = ram
#         print("Inside Smartphone constuctor")
    
  
# s=SmartPhone("Android",2)
# print(s.os)
# print(s.brand) #error come becouse parent class phone never call or never excute and variables are never initialise becouse child class init run

# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 2)Method overloading

# class Shape:
#     def area(self,radius):
#         return 3.14*radius*radius
    
#     def area(self,l,b):
#         return l*b
# s=Shape()
# # s.area(2) error method overloading is not work in python but work in java
# print(s.area(2,3))

# becouse python say we can do method overloading by default arrguments

# class Shape:

#     def area(self,a,b=0):
#         if b == 0:
#             return 3.14*a*a
#         else:
#             return a*b

# s = Shape()

# print(s.area(1))
# print(s.area(2,4))

# --------------------------------------------------------------------------------------------------------------

# 3)Operator OverLoading

print("hello" + "world")
print(4+5)
print([1,2,3]+[4,5])
