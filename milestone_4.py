# Hangman: Milestone 4

import random

class Hangman:

    def __init__(self, word_list, num_lives=5):

        self.chosen_word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.chosen_word]
        self.num_letters = len(set(self.chosen_word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []


# Create check guess, it checks if user-guess is in the chosen word.
    def check_guess(self, user_guess):

        guess = user_guess.lower()

        if guess in self.chosen_word:
            print(f"Good guess! '{user_guess}' is in the word.")
            for index, letter in enumerate(self.chosen_word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{user_guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left")


    # Create an ask for input function, asking user to enter a single letter guess.
    def ask_for_input(self):
    
        while True:
            user_guess = input('Enter your guess (a single letter): ')

            if len(user_guess) != 1 or not user_guess.isalpha():
                print('Invalid letter, Please, enter a single alphabetical character.')
            elif user_guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(user_guess)
                self.list_of_guesses.append(user_guess)
                break
