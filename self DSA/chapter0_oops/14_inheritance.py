# #parent
# class User:

#     def __init__(self):
#         self.name = 'nitish'

#     def login(self):
#         print('login')

# #child
# class Student(User):

#     def __init__(self):
#         self.rollno = 100

#     def enroll(self):
#         print('enroll into te course')

# u = User()
# s = Student()

# print(s.name)
# s.enroll()
# # print(s.rollno)
# s.login()
# -------------------------------------------------------------------------------------------------------------------------------------------------
#constructor example 1 :

# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera
    
#     def buy(self):
#         print("Buying a phone")

# class SmartPhone(Phone):
#     pass

# s=SmartPhone(2000, "Apple" ,13)
# s.buy()
# ---------------------------------------------------------------------------------------------------------------------------------------------
#constructor example 2

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

#child can't access private members of the class
# ----------------------------------------------------------------------------------------------------------------------------------------------------
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
    
#     def __show(self):
#         print (self.__price)

# class SmartPhone(Phone):
#     def check(self):
#         print(self.__price)

# s=SmartPhone(20000,"Apple",13)
# print(s.brand)
# s.check()#child class aceess all thing but not priavte data and methods
# s.__show()#i.e priavte method
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# class Parent:
    
#     def __init__(self,num):
#         self.__num = num
# #Getter
#     def get_num(self):
#         return self.__num
    
# class Child(Parent):

#     def show(self):
#         print("This is in child class")

# son = Child(100)
# print(son.get_num())
# son.show()
#if u have getter u can access private data also
# ----------------------------------------------------------------------------------------------------------------------------------------

# class Parent:

#     def __init__(self,num):
#         self.__num = num

#     def get_num(self):
#         return self.__num
    
# class Child(Parent):

#     def __init__(self,val,num):
#         self.__val = val

#     def get_val(self):
#         return self.__val

# son = Child(100,10)
# print("Parent: Num:",son.get_num()) # erro becouse child class have own constructor so parent constructor never call
# print("Chiild: val",son.get_val())
# --------------------------------------------------------------------------------------------------------------------------------
# class A:
#     def __init__(self):
#         self.var1 = 100

#     def display1(self,var1):
#         # self.var1 = var1
#         print("class A :", self.var1)

# class B(A):

#     def display2(self,var1):
#         print("class B :",self.var1)

# obj = B()
# obj.display1(200)
# obj.display1()
# ----------------------------------------------------------------------------------------------------------------------
#Method Overriding
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
    
#     def buy(self):
#         print("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print("Buying a smartphone")

# s = SmartPhone(220000, "Apple", 13)
# p = Phone(1000,"appel", "10px")
# # s.buy()
# p.buy()

# if same name thier is name method then child method is call
# ------------------------------------------------------------------------------------------------------------------------
#super method -> we can call parent 

# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
    
#     def buy(self):
#         print("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print("Buying a smartphone")
#         #synta to call parent ka buy method
#         super().buy()

# s = SmartPhone(220000, "Apple", 13)
# s.buy()

# ------------------------------------------------------------------------------------------------------------------------------------

# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Insdie phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

# class SmartPhone(Phone):
#     def __init__(self, price, brand, camera, os, ram):
#         print("Inside smartphone constructor")
#         super().__init__(price, brand, camera)
#         self.os = os
#         self.ram = ram
#         print("Inside smartphone constructor")

# s = SmartPhone(20000,"Samsung", 12, "Andriod", 2)

# print(s.os)
# print(s.brand)



# --------------------------------------------------------------------------------------------------------------------

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        #synta to call parent ka buy method
        super().buy()
s = SmartPhone(220000, "Apple", 13)
s.buy()

# -------------------------------------------------------------------------------------------------------------------

# class Parent:

#     def __init__(self,num):
#         self.__num = num
    
#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def __init__(self,num,val):
#         super().__init__(num)
#         self.__val = val
    
#     def get_val(self):
#         return self.__val
    
# son = Child(100,200)
# print(son.get_num())
# print(son.get_val())

# ---------------------------------------------------------------------------------------------------------------------

# class Parent:
#     def __init__(self):
#         self.num = 100

# class Child(Parent):

#     def __init__(self):
#         super().__init__()
#         self.var=200

#     def show(self):
#         print(self.num)
#         print(self.var)

# son = Child()
# son.show()


# -----------------------------------------------------------------------------------------------------------------
# Type of Inheritance

# 1)Single Inheritance
# 2)Multilevel Inheritance
# 3)Hierarchical Inheritance
# 4)Multiple Inheritance(Diamond Problem)
# 5)Hybrid Inheritance
# -------------------------------------------------------------------------------------------------------------------------
# 
#Single Inheritance
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
    
#     def buy(self):
#         print("Buying a phone")

# class SmartPhone(Phone):
#     pass
# SmartPhone(1000,"Apple","13px").buy()

# ----------------------------------------------------------------------------------------------------------------------------------
#multilevel
# class Product:
#     def review(self):
#         print("Product customer review")

# class Phone(Product):
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("buying a phone")

# class SmartPhone(Phone):
#     pass

# s=SmartPhone(2000,"apple",14)
# s.buy()
# s.review()

# ------------------------------------------------------------------------------------------------------------------------

#Hierarchical
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
    
#     def buy(self):
#         print("Buying a phone")

# class Smartphone(Phone):
#     pass

# class featurePhone(Phone):
#     pass

# Smartphone(1000,"apple",12).buy()
# featurePhone(2000,"sumsung",20).buy()

# ----------------------------------------------------------------------------------------------------------------------------------------
#Multiple
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brnad = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")
    
# class Product:
#     def review(self):
#         print("Customer review")

# class SmartPhone(Phone, Product):
#     pass 

# s = SmartPhone(1000,"Apple",10)
# s.buy()
# s.review()

# --------------------------------------------------------------------------------------------------------------------
# The Diamond Problem

#in this tyoe of problem which write first is called and other one is not called that is MRO method resolution order
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brnad = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")
    
# class Product:
#     def buy(self):
#         print("Customer review")

# class SmartPhone(Phone, Product):
#     pass 

# s = SmartPhone(1000,"Apple",10)
# s.buy()

# ----------------------------------------------------------------------------------------------------------------------------------

# problem 1

# class A:
#     def m1(self):
#         return 20
    
# class B :
#     def m1(self):
#         return 30
    
#     def m2(self):
#         return 40
    
# class C(B):
#     def m2(self):
#         return 20
    
# obj1 = A()
# obj2 = B()
# obj3 = C()
# print(obj1.m1() + obj3.m1() + obj3.m2())

#---------------------------------------------------------------------------------------------------------------------------------

# problem 2

# class A:

#     def m2(self):
#         return 20

# class B(A):

#     def m2(self):
#         val=super().m2()+30
#         return val
    
# class C(B):

#     def m1(self):
#         val = super().m2()+20
#         return val
    

# obj=C()
# print(obj.m1())


