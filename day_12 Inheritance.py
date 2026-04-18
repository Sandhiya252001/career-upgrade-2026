#Multilevel Inheritance
class Vehicle:
    def __init__(self):
        print("This is a vehicle class")
    def  start(self):
        print("Vehicle is starting")
    def accelerate(self):
        print("Providing acceleration to the vehicle")
    def gear(self):
        print("Its an auto-gear model")
class car(Vehicle):
    def __init__(self):
        super().__init__()
        print("This is a car")
    def model(self):
        self.model="Toyota"
        print(f"The model of car is {self.model}")
class fourWheeler(car):
    def __init__(self):
        super().__init__()
        print("This is a four Wheeler")
    def random(self):
        print("Happy riding")
#Multiple Inheritance    
# class car():
#     def __init__(self):
#         print("This is a car")
#     def model(self):
#         self.model="Toyota"
#         print(f"The model of car is {self.model}")
# class fourWheeler(Vehicle,car):
#     def __init__(self):
#          super().__init__()   // According to MRO it takes A as super class(left to right)
#         print("This is a four Wheeler")
#     def random(self):
#         print("Happy riding")

v1=Vehicle()
v1.start()
v2=car()
v2.accelerate()
v2.model()
v3=fourWheeler()
v3.gear()
v3.random()

      