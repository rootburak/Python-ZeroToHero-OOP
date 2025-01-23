
# meta class work when new class instance adding 
# Metaclasses are used to add and remove content from classes

class FirstMeta(type):
    def __new__(cls, name, bases, attrs): # __new__ means It works just before adding new instance
        def greeting(self):
            return "Hello !!!"
        
        #adding method
        attrs["greeting"] = greeting
        
        #adding variables
        attrs["name"] = "burak"
       
        return super().__new__(cls, name, bases, attrs)

class MyNewClass(metaclass=FirstMeta):
    pass
    
mynewclass = MyNewClass()
print(mynewclass.greeting())
print(mynewclass.name)

# new class with type first class name second base class name third attiributes
MyClass = type('MyClass', (), {
    'name': 'Emre',
    'method': lambda self: print('Greeting!!!')
})

myClass = MyClass()
print(myClass.name)
myClass.method()
