#13/50 python 50 exercises: printing tuple records

#?given this list of tuples, format it and return it as a string that looks like '{last name} {first name} {time}'
PEOPLE = [('Donald', 'Trump', 7.85),
           ('Vladimir', 'Putin', 3.626),
           ('Jinping', 'Xi', 10.603)]

from operator import itemgetter

def format_sort_records(tuples):
    output = [] #use list not string, bcs its easier to work with
    template = '{1:10} {0:10} {2:5.2f}' #template is a var with the value of this string with {n} inside, such that when template.format(*args) is passed, the [n] index of args substitutes {n}

    for person in sorted(tuples, key=itemgetter(1, 0)): #iterates thru a sorted version of tuples with the key of index (1), then (0)
        output.append(template.format(*person)) #appends person, which is each element of the list called tuples, to output list, formatted the way we want

    return output

print('\n'.join(format_sort_records(PEOPLE))) #'\n'.join joins the elements in the list into one string with a '\n' in between, which, when printed, separates them into new lines