# Task 1 Guess the Game

import random

games = ["Monopoly", "Uno", "Poker", "Life", "Snake and Ladder"]

selected_game = random.choice(games)

guess = input("Guess the selected game: ")
if guess.lower() == selected_game:
    print("Congratulations! You guessed correctly.")
else:
    print("Sorry, that's not correct. The selected game was:", selected_game)