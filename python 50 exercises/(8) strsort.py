#8/50 python 50 exercises: sorting a string

def strsort(string):
    return ''.join(sorted(string)) #sorted() sorts the characters of a string into a list in alphabetical bcs its a sequence, .join joins the list into one string

print(strsort("cbasklj"))