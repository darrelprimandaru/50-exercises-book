#7/50 python 50 exercises: ubbi dubbi

def ubbi_dubbi(string):
    output = '' #empty output string
    for i in string: 
        if i in 'aeiou':
            output += f'ub{i}' #if i is a vowel then add ub before i and concatenate it to output
        else:
            output += i #if i is not a vowel then just concatenate it to output
    return output

print(ubbi_dubbi("microsoft"))