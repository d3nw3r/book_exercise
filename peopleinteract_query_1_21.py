#interactuvni zaputu
import shelve
fieldsname = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldsname)
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')

    if not key: break
    try:
        record = db[key]
    except:
        print('No such key "%s"!'%key)
    else:
        for field in fieldsname:
            print(field.ljust(maxfield), '=>', getattr(record, field))
