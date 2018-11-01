import shelve
from person_1_15 import Person
from manager_1_16 import Manager

bob = Person('Bob Smith', 42, 40000)
sue = Person('Sue Jones', 4, 45000)
tom = Manager('Tom Taylor', 35, 50000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()
