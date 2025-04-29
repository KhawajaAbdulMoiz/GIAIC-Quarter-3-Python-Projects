# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    brand = ""
    def start(self):
        print(f"Car of the brand {self.brand} has been started")
        
car = Car()
car.brand  = "Toyota"
car.start()