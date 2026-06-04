# 2. Simple Example (No child constructor)
# Output:
# A Constructor
# 👉 Reason:
# Child (B) lo constructor ledu → Parent (A) constructor automatically call avuthundi.
class A:

    def __init__(self):
        print("A Constructor")


class B(A):
    pass


obj = B()

# ------------------
# 3. Child constructor unte?
class A:

    def __init__(self):
        print("A Constructor")


class B(A):

    def __init__(self):
        print("B Constructor")


obj = B()
# Output:
# B Constructor

# 👉 Reason:
# Child constructor parent ni override chesthundi.

# ------------------

# 4. Both constructors call cheyyali ante (super)
class A:

    def __init__(self):
        print("A Constructor")


class B(A):

    def __init__(self):
        super().__init__()   # Parent constructor call
        print("B Constructor")


obj = B()
# Output:
# A Constructor
# B Constructor

#---------------------------------------

# 5. Real World Example 🔥
class Person:

    def __init__(self, name):
        self.name = name
        print("Person Constructor")


class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        print("Employee Constructor")


e1 = Employee("Vishnu", 50000)

print(e1.name)
print(e1.salary)
# Output:
# Person Constructor
# Employee Constructor
# Vishnu
# 50000

#--------------------------