class User:
    def __init__(self, username, password):
        self.username = username # self parameter is a instance a User example user1
        if type(password) == int and password >= 5:
            self.password = password
        else:
            raise ValueError("Password must be an integer and greater than or equal to 5")

    #getter working when you reading the value
    def username(self):
        return self.username
    #getter
    def password(self):
        return self.password

    
    #setter working when you change the password here working . You can add some logics or methods
    def username(self,value):
        if type(value) == str:
            self.username = value
        else:
            raise ValueError("Username must be a string")

    #setter
    def password(self,newpass):
        if type(newpass) == int and newpass >= 5:
            self.password = newpass
        else:
            raise ValueError("Password must be an integer and greater than or equal to 5")


user1 = User(username="burak",password=12345)

print(user1.username)

print(user1.password)

user1.username="emre"
user1.password = 67890

print(user1.username)
print(user1.password)
