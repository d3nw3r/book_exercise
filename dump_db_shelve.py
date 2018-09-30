import shelve
from shelve import DbfilenameShelf

db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])
print(db['bob']['age'])
db.close()
