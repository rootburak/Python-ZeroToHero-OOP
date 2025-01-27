class Singleton():
_instance=None #globall variable
#cls equals self
    def __new__(cls, *args, **kwargs): # __new__ adding new instane 
    # if _instance not in memory 
        if not cls._instance:
            # add a new instance
            cls._instance = super(Singleton, cls).__new__(cls)
        # and return instance
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  
