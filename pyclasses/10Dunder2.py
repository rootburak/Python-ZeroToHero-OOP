class Setdelget():
    def __init__(self):
        self.data={}
    def __setitem__(self, key, value): #set item adding key value
        self.data[key]=value
                                
    def __delitem__(self, key):     #del item removing key value
        del self.data[key]
    
    def __getitem__(self, key):     #get item returning value
        return self.data[key]
    def __repr__(self):
        return str(self.data)

setdel = Setdelget()
setdel["one"] = 1
setdel["two"] = 2
setdel["three"] = 3
print(setdel)
del setdel["three"]
print(setdel)
print("get the two ",setdel["two"])



