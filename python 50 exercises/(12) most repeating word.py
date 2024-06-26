#12/50 python 50 exercises: word with most repeated letters

WORDS = ['this','is', 'an', 'elementary','test', 'example'] #given list of strings

from collections import Counter

def letter_count(word): #funct that calculates the number of most repeating letter in a word
    return Counter(word).most_common(1)[0][1] #counter() to count letters in each word, most_common() to sort the list of tuples greatest to least,
                                                #take the (1) tuple, [0] element of list, and [1] element of that [0] element, which is the number of times the most common letter appears

def most_repeating_word(strings_list):
    return max(strings_list, key=letter_count) #max() is the exact same as sorted() but it takes the first (min) or last (max) element

print(most_repeating_word(WORDS))