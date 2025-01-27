class Singleton(type):
    _instances = {}  # Instance checker

    # adding new instance with call
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:  # cls is a instance
            # add instances with key value
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Instance(metaclass=Singleton):
    # in real applications here maybe a dbaccess/orm
    def returnSelf(self):
        # return some string
        print(f"Hello! {self}")


# instances
singleton1 = Instance()
singleton2 = Instance()

print("s1 id", id(singleton1))
print("s2 id", id(singleton2))
singleton1.returnSelf()
singleton2.returnSelf()
# is checking s1 mem id and s2 mem id equal
print(singleton1 is singleton2)
