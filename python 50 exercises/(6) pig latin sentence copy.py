#6/50 python 50 exercises: pig latin sentence

def pl_sentence(sentence):
    translated = [] #empty list to append translated words
    for word in sentence.split(): #.split to split the input sentence into a list of words separated by whitespace
        if word[0] in 'aeiou':
            translated.append(f'{word}way')
        else:
            translated.append(f'{word[1:]}{word[0]}ay') #same exact code as exercise 5 but instead of return, append so it doesnt stop at the first word

    return ' '.join(translated) #.join to join the list of appended translated words into one sentence

print(pl_sentence("this is a test translation"))