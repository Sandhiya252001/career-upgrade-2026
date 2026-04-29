class Car:

    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def start(self):
        return f"{self.brand} {self.model} is starting."

    def accelerate(self, increase):
        self.speed = self.speed + increase
        return f"Speed increased. Current speed: {self.speed} km/h"

    def displayDetails(self):
        return f"""Car Details
Brand: {self.brand}
Model: {self.model}
Speed: {self.speed} km/h"""

# Creating multiple objects
car1 = Car("Maruti Suzuki", "XUV800", 100)
car2 = Car("Ford", "Fusion", 120)
car3 = Car("Toyota", "Corolla", 200)

# Calling methods
print(car1.start())
print(car1.accelerate(20))
print(car1.displayDetails())

print()

print(car2.start())
print(car2.displayDetails())

