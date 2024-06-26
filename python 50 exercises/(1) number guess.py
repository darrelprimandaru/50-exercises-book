#1/50 python 50 exercises: number guessing game

import random

def guessing_game():
    num = random.randint(1, 100) #inclusive
    while True: #infinite loop
        guess = int(input('pick 1-100: ')) #turn string input into int
        if num < guess:
            print('too high')
        if num > guess:
            print('too low')
        if num == guess:
            print('just right')
            break

guessing_game()