# ============================
# POLYMORPHISM + DUCK TYPING
# ============================


# --------- IDE CLASSES ---------

class Vscode:

    def execute(self):
        # VSCode executes compilation + running
        print("Compiling")
        print("Running")   # typo fixed explanation: Running


class MyEditor:

    def execute(self):
        # MyEditor does extra checks before execution
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


# --------- LAPTOP CLASS ---------
# Laptop doesn't care which IDE is used
# It only expects "execute()" method (Duck Typing)

class Laptop:

    def code(self, ide):
        # ide can be ANY object (Vscode / MyEditor etc.)
        # as long as it has execute() method
        ide.execute()


# --------- DUCK TYPING EXAMPLE ---------

class Duck:

    def speak(self):
        # Duck behavior
        print("Quack Quack")


class Dog:

    def speak(self):
        # Dog behavior
        print("Bark Bark")


class Cat:

    def speak(self):
        # Cat behavior
        print("Meow Meow")


# Common function for all animals
# No type checking → only checks speak() method

def animal_sound(animal):
    animal.speak()


# --------- OBJECT CREATION ---------

# Duck Typing demo
animal_sound(Duck())
animal_sound(Dog())
animal_sound(Cat())


# --------- IDE OBJECTS ---------

ide1 = Vscode()      # VSCode object
ide2 = MyEditor()    # MyEditor object

# --------- LAPTOP OBJECT ---------

lap1 = Laptop()
lap2 = Laptop()

# Laptop uses IDEs (Duck Typing in action)

lap1.code(ide2)   # MyEditor used
lap2.code(ide1)   # VSCode used