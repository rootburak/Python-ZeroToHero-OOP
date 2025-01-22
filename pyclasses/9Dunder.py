class Dunder():
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self): # iter for loop
        return self

    def __next__(self): # next oparations in for loop
        if self.current < self.max:
            self.current += 2
            return self.current 
            # the current increase by 2 
        else:
            raise StopIteration

for number in Dunder(10):
    print(number)           


class ReprDunder():
    def __init__(self,name):
        self.name = name
   
    def __repr__(self):
        return f'{self.name}' #returning a string 
repr = ReprDunder("burak")
print(repr)

class call():
    # __call__ class working like a function
    def __init__(self, name):
        self.name = name
    def __call__(self,name=""):
        if name == "":
            print(f'Hello {self.name}')
        else:
            print(f'Hello {name}')
instance = call("burak")
instance()
instance("Emre")
