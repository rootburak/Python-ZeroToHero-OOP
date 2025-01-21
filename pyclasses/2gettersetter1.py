class User():
    # Class definition
    def __init__(self, username, password):
        # Constructor method, called when a new User instance is added
        # It takes username and password parameters and assigns them to private variables.
        self._username = username  # Private variable (referance type and '_' name convention) _username
        self._password = password    # Private variable (referance type and '_' name convention) _password

    @property #getter with decorator 
    def username(self):
        # Getter method for username
        # Provides access to the value of _username from outside the class.
        return self._username

    @username.setter # setter with decorator
    def username(self, new_username):
        # Setter method for username
        # Used to assign a new value to _username from outside the class.
        # Checks if new_username is a string.
        if type(new_username) != str:
            raise ValueError("Username must be a string.")  # Raises an error if it's not a string
        self._username = new_username  # Updates _username if the new value is valid
    
    @property
    def password(self):
        # Getter method for password
        # Provides access to the value of _password from outside the class.
        return self._password

    @password.setter
    def password(self, new_password):
        # Setter method for password
        # Used to assign a new value to _password from outside the class.
        # Checks if new_password is an integer.
        if type(new_password) != int:
            raise ValueError("Password must be an int.")  # Raises an error if it's not an integer
        self._password = new_password  # Updates _password if the new value is valid

# new instance of the User class
user1 = User("burak", 12345)

# Printing the current username and password values
print(user1.username, user1.password)  # Output: burak 12345

# Updating the user's username
user1.username = "emre"  # Calls the setter method

# Updating the user's password
user1.password = 67890  # Calls the setter method

# Printing the updated username and password values
print(user1.username, user1.password)  # Output: emre 67890
