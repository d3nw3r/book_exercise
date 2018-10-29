from person_1_15 import Person
"""import class Person from person_1_15 """
class Manager(Person):
    """nasliduem class Person"""
    def giveRise(self, percent, bonus = 0.1):
        """zbilshuemo pay for manager percent+bonus"""
        self.pay *= (1.0 + percent + bonus)

tom = Manager(name = 'Tom York', age = 45, pay = 50000)
print(tom.lastName())
tom.giveRise(0.25)
print(tom.pay)

