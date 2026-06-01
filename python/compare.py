class Human:

    def __init__(self):
        self.name = "vishnu"
        self.age = 21
    

    def compare(self , other):
        if c1.age == c2.age:
            return True
        else:
            False
    
    def update(self, age):
        self.age = age

c1 = Human()
c1.update(31113)
c2 = Human()


if c1.compare(c2):
    print("True")
else:
    print("False")

print(c1.age)