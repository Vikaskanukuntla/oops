class car:

    wheels = 5 #class variable or static variable

    def __init__(self):
        self.name = "BMW"  #instance variable
        self.mil = "10"    #instance variable

    def drive(self):
        print("car is in driving mode")


c1 = car()
c2 = car()
c1.mil = 22

car.wheels = 2
print(c1.wheels , c2.wheels)  