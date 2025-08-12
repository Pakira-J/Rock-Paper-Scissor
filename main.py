# This is my first game in python.
# Name of the game: Rock, Paper, Scissors
# Author: Joydeep Pakira
# Date: 2023-10-01

import random


def game_choice():
    player_choice = input(
        "Enter your choice [rock, paper, scissors] : ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    choice = {"player": player_choice, "computer": computer_choice}
    return choice


def game_win(player, computer):
    if player == "rock" or player == "paper" or player == "scissors":
        print(f"Player --> {player} :: Computer --> {computer}")
        if player == computer:
            return "It's a tie!"
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") \
                or (player == "scissors" and computer == "paper"):
            return "Congrats! Player wins."
        else:
            return "Try again. Computer wins."
    else:
        return "Invalid input. Try again."


gameplay = game_choice()
print(game_win(gameplay["player"], gameplay["computer"]))
