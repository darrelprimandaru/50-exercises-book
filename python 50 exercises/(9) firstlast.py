#9/50 python 50 exercises: first-last

def firstlast(sequence):
    return sequence[:1] + sequence[-1:] #use slice instead of index bcs index returns the type of the indexed value while slice returns the same type as the entire sequence

list = ['a', 'b', 'c', 4]
print(firstlast(list))