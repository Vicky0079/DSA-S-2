class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
# outside the class --> function

def greet(person):
    print('Hi my name is',person.name,'and I am a',person.gender)
    p1 = Person('ankit','male')
    return p1

p = Person('nitish','male')
x = greet(p)
print(x.name)
print(x.gender)