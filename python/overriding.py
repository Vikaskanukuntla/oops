# Method Overriding
# Definition

# Child class parent class method ni own implementation tho replace cheyyadam.

# -----------------------------------------------
# Parent Class
class Animal:

    def sound(self):
        print("Animal makes a sound")


# Child Class
class Dog(Animal):

    # Overriding Parent Method
    def sound(self):
        print("Dog Barks")


obj = Dog()

# Child method executes
obj.sound()

# Output
# Dog Barks


# Python first checks:

# Dog class lo sound() undha?

# ✅ Yes

# So:

# print("Dog Bark")

# execute chesthundi.

# Parent method ni ignore chesthundi.

# --------------------------------------

# If Child Doesn't Have Method
# class Animal:

#     def sound(self):
#         print("Animal Sound")


# class Dog(Animal):
#     pass


# obj = Dog()
# obj.sound()
# Output
# Animal Sound

# --------------------------------------
# Python search order:

# Dog → Animal

# Dog lo method lekapothe parent daggara ki velthundi.
# --------------------------------------

# """Using super()

# Konni sarlu parent functionality kuda kavali."""

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        # Call Parent Method
        super().sound()

        print("Dog Bark")


obj = Dog()
obj.sound()


# Output
# Animal Sound
# Dog Bark
# --------------------------------------