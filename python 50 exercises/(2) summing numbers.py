#2/50 python 50 exercises: summing numbers

def mysum(*numbers):
    output = 0
    for i in numbers:
        output += i

    return output

print(mysum(3, 4, 5)) #example output