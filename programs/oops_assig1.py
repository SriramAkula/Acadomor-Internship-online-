class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

car = Car("BMW", "BMW-model", 2022)
bike = Bike("Yamaha", "YAM-model", 2023)

car.start_engine() 
bike.start_engine() 
