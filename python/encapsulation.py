# What is Encapsulation?

# Simple definition:

# Data (variables) and methods ni oka unit (class) lo bundle cheyyadam and direct access ni control cheyyadam.
# -------------------------------------------------------------------
# Why Encapsulation?

# Imagine:

# class Student:

#     def __init__(self):
#         self.marks = 90
# s1 = Student()

# s1.marks = -500

# Marks negative avvakudadhu 😭

# Kani direct ga modify chesam.

# Solution:

# Hide data
# ↓
# Provide controlled access
# -------------------------------------------------------------------
# Access Modifiers in Python

# Python lo strict access modifiers levu.

# Convention-based.

# Modifier	Syntax	Access
# Public	name	Anywhere
# Protected	_name	Inside class & child
# Private	__name	Inside class only
# -------------------------------------------------------------------
# 1. Public Variable

class Student:

    def __init__(self):
        self.name = "Vishnu"

# Usage:

s1 = Student()

print(s1.name)

# Output:

# Vishnu

# Accessible everywhere.

# -------------------------------------------------------------------
# 2. Protected Variable

# Single underscore.

class Student:

    def __init__(self):
        self._name = "Vishnu"

# Usage:

s1 = Student()

print(s1._name)

# Output:

# Vishnu
# Important

# Python prevent cheyyadu.

# Just convention:

# "Please don't access directly"
# -------------------------------------------------------------------

# 3. Private Variable ⭐

# Double underscore.

class Student:

    def __init__(self):
        self.__marks = 90

# Usage:

s1 = Student()

print(s1.__marks)

# Error:

# AttributeError
# -------------------------------------------------------------------

# Real Encapsulation Example

# Employee salary.

# Wrong Design
class Employee:

    def __init__(self):
        self.salary = 50000

# Anyone can do:
#emp = Employee()
# # emp.salary = -1000

# Bad.

# --------------------

# Encapsulation Design
class Employee:

    def __init__(self):
        self.__salary = 50000

    def getSalary(self):
        return self.__salary

    def setSalary(self, amount):

        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid Salary")

# Usage:

emp = Employee()

print(emp.getSalary())

emp.setSalary(70000)

print(emp.getSalary())

# Output:

# 50000
# 70000
# Invalid Update
emp.setSalary(-5000)

# Output:

# Invalid Salary

# Now data protected.
# -------------------------------------------------------------------
# Getter & Setter Concept
# Getter

# Read value.

def getSalary(self):
    return self.__salary
# Setter

# Modify value safely.

def setSalary(self, amount):

    return

# Validation add cheyyachu.
# -------------------------------------------------------------------
# Pythonic Way (Property)

# Instead of:

# getSalary()
# setSalary()

# Modern Python:

class Employee22:

    def __init__(self):
        self.__salary = 50000

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):

        if value > 0:
            self.__salary = value
        else:
            print("Invalid Salary")

# Usage:

emp = Employee22()

print(emp.salary)

emp.salary = 80000

print(emp.salary)

# Looks like normal variable access but validation happens.
# -------------------------------------------------------------------

# Encapsulation + Inheritance
class A:

    def __init__(self):
        self.__x = 10


class B(A):

    def show(self):
        print(self.__x)

# Error.

# Because:

# Private members are not inherited directly
# Protected Works
class A:

    def __init__(self):
        self._x = 10


class B(A):

    def show(self):
        print(self._x)

# Output:

# 10
# -------------------------------------------------------------------

# Real World Example

# Bank Account

class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def showBalance(self):
        print(self.__balance)

# Usage:

acc = BankAccount()

acc.deposit(500)

acc.withdraw(300)

acc.showBalance()

# Output:

# 1200
# -------------------------------------------------------------------

# Difference: Public vs Protected vs Private
# self.name      # Public

# self._name     # Protected

# self.__name    # Private
# Type	Accessible Outside?
# Public	✅ Yes
# Protected	✅ Yes (Convention)
# Private	❌ No (Directly)
# -------------------------------------------------------------------

# Private Variable
class Student:

    def __init__(self):
        self.__marks = 90


s = Student()

print(s.__marks)

# Output: AttributeError

# Ikkada confusion start avuthundi 😄

# Nuvvu anukuntav:

# __marks delete aipoyinda?

# ❌ No.

# Python Internally Em Chesthundi?

# Python:

# self.__marks

# ni

# self._Student__marks

# ga rename chesthundi.

# Idi Name Mangling.

# Visualization

# Nuvvu rasindi:

# __marks

# Python memory lo pettedhi:

# _Student__marks



# Proof
class Student:

    def __init__(self):
        self.__marks = 90


s = Student()

print(s._Student__marks)

# Output:

# 90

# 😲 Variable undi!

# Kani peru marchindi.


# Why Python Ila Chesthundi?

# Imagine:

class BankAccount:

    def __init__(self):
        self.__balance = 10000

# Outside:

acc = BankAccount()

acc.__balance = 0

# Python wants to avoid accidental access.

# So:

# __balance
# ↓
# _BankAccount__balance

# ani rename chesthundi.

#-----------------------------
# Check Memory
class Student:

    def __init__(self):
        self.__marks = 90


s = Student()

print(s.__dict__)

# Output:

# {'_Student__marks': 90}

# 🔥 Idi best proof.

# Nuvvu __marks create chesav.

# Memory lo:

# _Student__marks

# store ayindi.
#-----------------------------