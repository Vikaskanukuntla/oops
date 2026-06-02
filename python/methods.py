class Employee:

    company = "Google"

    # 1. Instance Method
    # When to use?
    # Object ki sambandhinchina data kavali.
    # Example:
    # Employee name print cheyyali
    # Salary print cheyyali

    # Why Instance Method?
    # Because every employee has different:
    # name
    # salary
    # Method needs object data.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def showDetails(self):  # Instance Method
        print("Name:", self.name)
        print("Salary:", self.salary)


    # ------------------ *** ---------------

    # 2. Class Method
    # When to use?
    # Class-level data ni access or modify cheyyali.
    # Example:
    # Company name andariki same.


    # Why Class Method?

    # Because company belongs to the class, not to individual employees.

    # Employee 1 salary → Different
    # Employee 2 salary → Different

    # Company → Same for all employees

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany
    
    def info(cls):
        print(cls.company)

    # ------------------ *** ---------------

    # 3. Static Method
    # When to use?

    # Method neither needs:

    # self
    # nor
    # cls

    # But logically belongs to the class.
    @staticmethod
    def isEligible(age):
        return age >= 18


e1 = Employee("Vishnu", 50000)
e2 = Employee("Arya", 70000)

e1.showDetails()

e1.info()

# Employee.changeCompany("Microsoft")

# print("Company:", Employee.company)

# print(Employee.isEligible(21))