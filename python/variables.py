class car:

    wheels = 5

    def __init__(self):
        self.name = "BMW"
        self.mil = "10"

    def drive(self):
        print("car is in driving mode")


c1 = car()
c2 = car()
c1.mil = 22

car.wheels = 2
print(c1.wheels , c2.wheels)  