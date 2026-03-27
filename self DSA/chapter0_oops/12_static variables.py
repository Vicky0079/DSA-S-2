#instance variable 
# is for object and value is differ for differ object
#  & when we use instance variable we use object name with it like self
#object name. variable name is instance variable

# static variable
# 
# is for class and same value like roll no.,ifce bank no.,collage name
#  & when we use static variable we use class name with it like here Atm
#class name . variablde name is static variable
class  Atm:

    __counter = 0

    # constructor(special function)->superpower ->
    def __init__(self):
        # print(id(self)) 
        self.pin  = ''
        self.balance = 0
        # print('mai to execute ho gaya')
        # self.menu()
        self.cid = Atm.__counter   
        Atm.__counter = Atm.__counter + 1

    #utility function
    @staticmethod
    def get_counter():
        return Atm._counter
    
    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit 
        """)           

        if user_input == '1':
          #create pin
          self.create_pin()
        elif user_input == '2':
          #change pin
          self.change_pin()

        elif user_input =='3':
            #check balance
            self.check_balance()
            
        elif user_input == '4':
            #withdraw
           self.withdraw()  
        else:
            exit()
    
    def create_pin(self):
       user_pin = input('enter your pin')
       self.pin = user_pin

       user_balance = int(input('enter balance'))
       self.balance = user_balance

       print('pin created successfully')
       self.menu()

    def change_pin(self):
        old_pin = input('Enter your old pin')

        if old_pin == self.pin:
            # let him chnage the pin
            new_pin = input("Enter new pin")
            self.pin = new_pin
            print('pin change successful')
            self.menu()
            
        else:
            print('nai karne de sakata re baba')
            self.menu()
    def check_balance(self):
        user_pin = input("Enter your pin ")
        if user_pin == self.pin:
            print("your balance is ",self.balance)
        else:
            print("chal nikal yahan se")

    def withdraw(self):
        user_pin = input("Enter the pin")
        if user_pin == self.pin:
            #allow to wihdraw
            amount = int(input("enter the amount"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdrawl successful balance is ",self.balance)
                
            else:
                print('Abe garib')
            # self.menu
        else:
            print("sale chor")
        self.menu()

obj = Atm()
# print(id(obj))

# print(type(obj))
Atm.counter = 'hehehehhe'
c1 = Atm()
c2 = Atm()
c3 = Atm()
print(Atm.get_counter)
# print(c2.cid)
# print(c3.cid)
# print(Atm.counter)







