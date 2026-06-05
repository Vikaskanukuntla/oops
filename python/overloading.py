class calculator:

    def add(self , a , b , c = 0 , d = 0 , e = 0 , f = 0):
        print("sum = " , a+b+c+d+e+f)


c1 = calculator()
c1.add(1,2,3)
c1.add(1,2,3,3,4,3)
c1.add(1,2,3,3,4)
c1.add(1,2,3,3)
c1.add(1,2)


#-------------------------------

class Calculator1:

    def add(self, *nums):
        return sum(nums)
obj = Calculator1()

print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add(1,2,3,4))

# output
# 3
# 6
# 10

# ----------------------------
# *args vs **kwargs
# *args → extra positional arguments ni tuple ga collect chesthundi.
# **kwargs → extra keyword arguments ni dictionary ga collect chesthundi.
def details(**kwargs):
    print(kwargs)

details(name="Vikas", age=22, city="Hyderabad")

# Output:

# {'name': 'Vikas', 'age': 22, 'city': 'Hyderabad'}

# -----------------------------------------------

class Employee:

    def show(self, **kwargs):
        if "name" in kwargs and "age" in kwargs:
            print(f"Name: {kwargs['name']}, Age: {kwargs['age']}")

        elif "name" in kwargs:
            print(f"Name: {kwargs['name']}")

obj = Employee()

obj.show(name="Vikas")
obj.show(name="Vikas", age=22)

# Name: Vikas
# Name: Vikas, Age: 22

# -----------------------------------------------

# ----------- important ---------------

class Demo:

    # First method
    def add(self, a, b):
        print("First Method")
        return a + b

    # Same name again
    # Python sees this and replaces the previous add()
    def add(self, a, b, c):
        print("Second Method")
        return a + b + c


obj = Demo()

# Calls the only add() method that exists now
print(obj.add(10, 20, 30))

# Output
# Second Method
# 60


# What Actually Happens Internally
class Demo:

    def add(self, a, b):
        pass

    # Old add() removed
    # New add() stored
    def add(self, a, b, c):
        pass

# Python internally treats it almost like:

class Demo:
    pass


# Store method named add
# Demo.add = first_method

# Same name again
# Previous reference overwritten
# Demo.add = second_method

# Final ga class lo:

# add --> second_method

# matrame untundi.

# Proof
class Demo:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


obj = Demo()

# Python expects 3 arguments
print(obj.add(1, 2))
# Error
# TypeError:
# Demo.add() missing 1 required positional argument: 'c'

# Enduku?

# Because first method already delete/overwrite aipoyindi.