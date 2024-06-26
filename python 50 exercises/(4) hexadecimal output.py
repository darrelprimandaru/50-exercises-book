#4/50 python 50 exercises: hexadecimal output

def hex_output():
    dec = 0
    hex = input("Enter hex nubmer: ") #user input
    for power, digit in enumerate(reversed((hex))): #enumerate gives each iteration of for loop as a tuple with this structure: [index, iterated digit]
        dec += int(digit, 16) * (16 ** power) #turn each digit of reversed user input into a base 16 int, multiply by 16 to the index power (that's why it's reversed)
    print(dec)

hex_output()