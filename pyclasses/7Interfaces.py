from abc import ABC , abstractmethod

class Product(ABC):
    
    @abstractmethod
    def calculate_cost(self,price,cost):
        pass
    
    @abstractmethod
    def display_details(self,name,price):
        pass
    

class ProductA(Product):
    def __init__(self,price,cost,name):
        self.name = name
        self.price = price
        self.cost = cost
    
    def calculate_cost(self,price,cost):
        self.price = price-cost
    
    def display_details(self, name, price):
        print(f"Product A: {name}, Price: {price}")

