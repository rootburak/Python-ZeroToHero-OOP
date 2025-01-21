class Person(): # Person is a object like strings integers every think is a object in python

    name = None
    age = None

    def __init__(self, name, age): # __init__ is a special method in Python classes that gets called when a new object is added
        self.name = name #self a referance the attribute example newPerson = Person() self is newPerson
        self.age = age
    def printNameAndAge(self): # self class scope
        print(f'Name: {self.name}, Age: {self.age}')

# New Instance 
person1 =Person(name="burak",age=20)

person1.printNameAndAge() # attiributes the person example string.upper()





example = "name" # new str class 

print(example)

example = example.upper() # str class attributes

print(example)
