import shelve
db = shelve.open('class-shelve')

sue = db['sue']
sue.giveRise(0.25)
db['sue'] = sue

tom = db['tom']
tom.giveRise(0.2)
db['tom'] = tom

db.close()