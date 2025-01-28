# Factory Design Pattern

"""Imagine you're at a car dealership. You want to buy a new car, but you're not sure which type of car you want. You can choose from a variety of models, such as a Toyota, Ford, or Honda. Each model has its own unique features and characteristics.

In this scenario, the car dealership is like a factory. The factory produces different types of cars, each with its own unique features. You, the customer, don't need to know how the cars are made or what features they have. You just need to tell the factory what type of car you want, and they will produce it for you.

This is similar to how the Factory Pattern works in programming. The factory is a class that produces different types of objects, each with its own unique features. You, the programmer, don't need to know how the objects are made it or what features they have. You just need to tell the factory what type of object you want, and it will make it for you. """


# Car.py (Interface)
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}"

# Sedan.py (Concrete Class)


class Sedan(Car):
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_info(self):
        return f"Sedan: {self.make} {self.model}"

# SUV.py (Concrete Class)


class SUV(Car):
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_info(self):
        return f"SUV: {self.make} {self.model}"

# Truck.py (Concrete Class)


class Truck(Car):
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_info(self):
        return f"Truck: {self.make} {self.model}"

# CarFactory.py (Factory Class)


class CarFactory:
    @staticmethod
    def new_car(make, model, type):
        if type == "sedan":
            return Sedan(make, model)
        elif type == "suv":
            return SUV(make, model)
        elif type == "truck":
            return Truck(make, model)
        else:
            return None

# Main.py (Client Class)


def main():
    sedan = CarFactory.new_car("Toyota", "Corolla", "sedan")
    print(sedan.get_info())  # Output: Sedan: Toyota Corolla

    suv = CarFactory.new_car("Honda", "CR-V", "suv")
    print(suv.get_info())  # Output: SUV: Honda CR-V

    truck = CarFactory.new_car("Ford", "F-150", "truck")
    print(truck.get_info())  # Output: Truck: Ford F-150


if __name__ == "__main__":
    main()
