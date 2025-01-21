class User():
    # This method initializes a new instance of the User class
    # Self is user1 user1 =User()
    def __init__(self, username, password):
        self._username = username  # This is a private (name convention) attribute for the username
        self._password = password  # This is a private (name convention) attribute for the password

    # This method changes the username to uppercase
    def upperCase(self):
        self._username = self._username.upper()  # Convert the username to uppercase
        return self._username  # Return the modified username

    # This method returns a string containing the username and password
    def secretKey(self):
        return f"{self._username} your secret key = {self._password}"  # Format the output string

    # This property allows access to the username
    @property
    def username(self):
        return self._username  # Return the private username

    # This setter allows modification of the username
    @username.setter
    def username(self, new_username):
        self._username = new_username  # Update the private username with a new value

# An instance of the User class is instantiated with a username and password
user = User("burak", 12345)

# Call the upperCase method and print the result
print(user.upperCase())  # Output: BURAK

# Change the username using the setter
user.username = "emre"

# Call the secretKey method and print the result
print(user.secretKey())  # Output: EMRE your secret key = 12345

# _username is the private but you can change it not recommended this is for python's flexibility
user._username = "ali"  # renamed _username
print(user.username)  # Output: ali 

