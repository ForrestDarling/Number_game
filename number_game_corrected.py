#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math

__author__ = "Forrest Darling"

# Create empty list to use in show_score function
attempt_list = []


# Funtion to show high score or gives arbitrary message if no high score yet recorded.
def show_score():
    if not attempt_list:
        print("You know this other guy got it in like two tries.")
        attempt_list.append(2)
    else:
        print("The current high score is {} attempts".format(min(attempt_list)))

# Function to print greeting message and receive user input for name.
# Check if user input is an empty string to either format game details or print message without name.
def name_input():
    print("Hello fellow traveler, welcome to the guessing game.")
    user_name = input("What is your name?")

    if user_name != "":
        return print("Nice to meet you {}. Want to play a game? In this game you guess a number between 1 and 10."
            .format(user_name))
    else:
        return print("Alright then keep your secrets. Want to play a game? In this game you guess a number "
                     "between 1 and 10.")

# Function to take user input to determine if game restarts or if module ends.
# This function also determines whether user input is an empty string or if input is not 'yes' or 'no'.
# This also contains one of two exit() functions along with the want_to_play_again() function.
def ready_to_play():
    ready_play = input("Are you ready to play (yes/no)?")

    while True:
        if ready_play == "":
            ready_play = input("Please enter yes/no:")
        elif ready_play.lower() not in ["yes", "no"]:
            ready_play = input("Please enter yes/no:")
        else:
            break

    if ready_play.lower() != "yes":
        print("Ok goodbye fellow traveler.")
        exit()
    elif ready_play.lower() == "yes":
        return ready_play == "yes"

# This is the main function to run the meat of the game. After declaring the variables it creates a list of numbers
# to ensure user input is within admissable range.
def execute_guess():
    rand_num = random.randint(1, 10)
    attempts = 0
    range_of = []
    for i in range(1, 11):
        range_of.append(i)

    # This While loop takes the user input and ensures it is valid guess (meaning in between 1 and 10 as well and an
    # int). After each guess one is added to attempts and the new high score is added to attempt list.
    while True:
        try:
            guess = math.floor(float(input("Please guess a number between 1 and 10:")))
            if math.floor(guess) in range_of:
                if guess == rand_num:
                    attempts += 1
                    attempt_list.append(attempts)
                    print("Correct! Great job you guessed right in {} attempts".format(attempts))
                    want_to_play_again()
                else:
                    attempts += 1
                    attempt_list.append(attempts)
                    print("Sorry {} is incorrect try again.".format(guess))
                    continue
            else:
                print("{} is not in between 1 and 10 please guess again:".format(guess))
                attempts += 1
                attempt_list.append(attempts)
                continue
        except ValueError:
            print("Please enter a valid number:")
            attempts += 1


# This function takes user input and allows user to exit the game or play again and restart with execute_guess().
# This contains one of two exit() functions in this code the other is in want to play.
def want_to_play_again():
    play_again = input("Would you like to play again? (yes/no)").lower()
    while True:
        if play_again == "" or play_again not in ["yes", "no"]:
            play_again = input("Please enter yes/no:")
        else:
            break
    if play_again != "yes":
        print("OK goodbye have a great day.")
        exit()
    else:
        execute_guess()

# Main function to run game
def start_game():

    name_input()

    ready_to_play()

    show_score()

    execute_guess()



# Calls main funciton
if __name__ == "__main__":
    start_game()