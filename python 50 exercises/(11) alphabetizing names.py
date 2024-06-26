#11/50 python 50 exercises: alphabetizing names

import operator

PEOPLE = [{'first':'Reuven', 'last':'Lerner',
            'email':'reuven@lerner.co.il'},
            {'first':'Donald', 'last':'Trump',
            'email':'president@whitehouse.gov'},
            {'first':'Vladimir', 'last':'Putin',
            'email':'president@kremvax.ru'}
            ] #given constant, list of dicts

def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first')) #return sorted list of dicts by a specific key, which is the function 
                                                                            #itemgetter that can get the specific definitions of a dict, in this case 'last', 'first'
  
print(alphabetize_names(PEOPLE))