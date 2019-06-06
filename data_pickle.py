'''
import pickle

with open('mydata.pickle','wb') as mysavedata:
    pickle.dump([1,2,'three'],mysavedata)

with open('mydata.pickle','rb') as myrestoredata:
    a_list = pickle.load(myrestoredata)

print(a_list)
'''


import pickle
from list_print_function import print_lol

new_man = []

try:
    with open('man_data.txt','rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error:' + str(err))
except PickleError as perr:
    print('Pickling error:' + str(perr))

print_lol(new_man)

