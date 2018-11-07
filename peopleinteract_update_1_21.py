#interactuvni zaputu
import shelve
from person_1_15 import Person
fieldsname = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldsname)

db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')

    if not key: break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldsname:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>'%(field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key]=record
db.close()