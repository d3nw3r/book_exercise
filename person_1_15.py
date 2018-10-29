class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        """return lastname"""
        return self.name.split()[-1]

    def giveRise(self, percent):
        """rise pay + percent"""
        self.pay *= (1.0 + percent)


"""bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
print(bob.name, sue.name)

print(bob.lastName())
sue.giveRise(0.1)
print(sue.pay)
"""