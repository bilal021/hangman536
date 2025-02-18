# Hangman: Milestone 3

import random 

word_list = ['Apple', 'Banana', 'Blueberry', 'Kiwi', 'Strawberry']

chosen_word = random.choice(word_list).lower()


# Ask the user to enter a single word
user_guess = input('Entre your guess: ')

# Validate the input
if len(user_guess) == 1 and user_guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')

# Create check guess, it checks if user-guess is in the chosen word
def check_guess(user_guess):

    guess = user_guess.lower()

    if guess in chosen_word:
        print(f"Good guess! '{user_guess}' is in the word.")
    else:
        print(f"Sorry, '{user_guess}' is not in the word.")

    return user_guess

def ask_for_input():
    
    while True:
        user_guess = input('Enter your guess in a single letter: ')
        if len(user_guess) == 1 and user_guess.isalpha():
            break
        else:
            print('Invalid letter, Please, enter a single alphabetical character.')
        check_guess(user_guess)

        break

ask_for_input()
