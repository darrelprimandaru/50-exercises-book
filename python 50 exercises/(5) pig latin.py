#5/50 python 50 exercises: pig latin

def pig_latin():
    string = input("Enter a word: ")
    if string[0] in "aeiou": #main takeaway, just use -- in 'string' -- to check if a character is in a string
        string = f"{string}way"
        print(string)
    else:
        string = string[1:] + "ay" #don't need to do string = string, you can just return the proper string and put print() outside the if for less lines
        print(string)
        

pig_latin()