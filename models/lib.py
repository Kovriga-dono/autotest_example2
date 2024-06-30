import random
import string

catt = ('Friends', 'Coworkers', 'Family', 'Business', 'Contacts')

class Filling:

    def letters(x):
        let = (random.choice(string.ascii_lowercase) for x in range(5))
        return let


    def numbers(x):
        num = (random.choice(string.digits) for x in range(x))
        return num


    def categ():
        cho = (random.choice(catt))
        return cho
