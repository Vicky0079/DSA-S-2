class Person:

    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == 'india':
            print('Namaste',self.name)
        else:
            print('Hello',self.name)

# how to acces attributes:
P = Person('nitish','india')
P.gender = 'male'
# print(P.country)
# print(P.name)
# P.greet()
print(P.gender)
print(P.name)