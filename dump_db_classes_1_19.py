import shelve
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n', db[key].name, 'has s pay = ', db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())
