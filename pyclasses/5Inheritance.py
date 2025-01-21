class Customer():

    def __init__(self, name, email):
        self._name = name
        self._email = email
    @property
    def name(self):
        return self._name
    @property
    def email(self):
        return self._email
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string.")
        self._name = new_name
    @email.setter
    def email(self, new_email):
        if not isinstance(new_email, str) or not "@" in new_email:
            raise ValueError("Email must be a string and contain '@'.")
        self._email = new_email


    # IMPORTANT OVERRIDE FUNCTION
    def details(self):
        return f"Name: {self.name}, Email: {self.email}"

class IndividualCustomer(Customer):
    def __init__(self, name, email, age):
        super().__init__(name, email) #super sending name and email Customer __init__
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or new_age < 0:
            raise ValueError("Age must be a non-negative integer.")
        self._age = new_age

    # OVERRIDE HERE 
    def details(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"

class CorporateCustomer(Customer):
    def __init__(self, name, email, company_name):
        super().__init__(name, email)
        self._company_name = company_name
    @property
    def company_name(self):
        return self._company_name

    def details(self):
        return f"Name: {self.name}, Email: {self.email}, Company: {self.company_name}" 

Customer1 = IndividualCustomer(name="burak",email="burak@root.com",age=20)
Customer2 = CorporateCustomer(name="emre",email="emre@root.com",company_name="emre's company")

print(Customer1.details())
print(Customer2.details())
