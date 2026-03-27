class Person:

    def __init__(self):
        self.name = 'nitish'
        self.gender = 'male'

# Person() # here object is created
# print(Person().name)

P = Person()
Q = P
print(P.name)
print(Q.name)
Q.name = 'vicky'
print(Q.name)
print(P.name)

                                                                                                                                                                             