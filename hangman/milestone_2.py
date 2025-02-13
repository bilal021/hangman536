# Hangman: Milestone 2

import random 


word_list = ['Apple', 'Banana', 'Blueberry', 'Kiwi', 'Strawberry']

word = random.choice(word_list)

guess = input('Entre your guess: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')


print(guess)

#print(word_list)