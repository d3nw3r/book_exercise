from person_1_15 import Person
from manager_1_16 import Manager

bob = Person('Bob Jones', 45, 4000)
sue = Person('Sue Bib', 40, 3500)
tom = Manager('Tom York', 35, 4500)

db = [bob, sue, tom]

for i in db:
    i.giveRise(0.1)

for i in db:
    print(i.lastName() + " => " + str(i.pay))
