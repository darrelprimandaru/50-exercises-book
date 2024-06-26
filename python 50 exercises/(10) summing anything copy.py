#10/50 python 50 exercises: summing anything

def mysum(*input):
    if not input:
        return input #2nd condition, return empty tuple if empty tuple is inputted
    
    output = input[0] #start output with index 0 of input
    for i in input[1:]: #for each element in input starting from index 1 to the very last,
        output += i     #add or concatenate i to output
    return output

print(mysum(1, 4, 5))
print(mysum(['a', 'b', 'c', 'd']))