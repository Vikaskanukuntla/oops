class Student:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks


s1 = Student(50)
s2 = Student(70)

result = s1 + s2

print(result)

# Output:
# 120

# 💡 What happened internally?
# s1 + s2
# ↓
# s1.__add__(s2)



class Student:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return Student(self.marks + other.marks)

    def show(self):
        print(self.marks)


s1 = Student(40)
s2 = Student(60)

s3 = s1 + s2

s3.show()
# Output:
# 100


# 🔥 Example 3: String-like behavior (custom)
class Book:

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def show(self):
        print("Total Pages:", self.pages)


b1 = Book(100)
b2 = Book(200)

b3 = b1 + b2

b3.show()
# Output:
# Total Pages: 300