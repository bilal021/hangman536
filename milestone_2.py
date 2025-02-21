# Hangman: Milestone 2

import random 


word_list = ['Apple', 'Banana', 'Blueberry', 'Kiwi', 'Strawberry']
chosen_word = random.choice(word_list)
print(chosen_word)

# Ask the user to enter a single word
user_guess = input('Entre your guess: ')

# Validate the input
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
