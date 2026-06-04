class A:

    def feature1(self):
        print("feature1")

    def feature2(self):
        print("feature2")

class B(A):

    def feature3(self):
        print("feature3")

    def feature4(self):
        print("feature4")

class C(B):

    def feature5(self):
        print("feature 5")


# ---------------------------
# multiple 


# Search order:

# C
# ↓
# A  ✅ Found
# ↓
# B
# ↓
# object

# Anduke "A Show" print avuthundi

class A1:

    def show(self):
        print("A Show")


class B1:

    def show(self):
        print("B Show")


class C1(A1, B1):
    pass


obj = C()
obj.show()














b1 = B()
c1 = C()


b1.feature1()
b1.feature3()
c1.feature1()