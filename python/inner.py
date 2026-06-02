class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name , self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8"

        def show(self):
            print(self.brand, self.cpu, self.ram)

class Student1:

    def __init__(self,brand , cpu , ram):
        self.Lap = self.Laptop1(brand , cpu , ram)

    class Laptop1:

        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
        
        def show(self):
            print(self.brand, self.cpu, self.ram)
         



# s1 = Student("navin" , 21)
# s1.show()

# s1.lap.show()


s2 = Student1("asus" , "i5" , "16")
# s2.Lap()
s2.Lap.show()