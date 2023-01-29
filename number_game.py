#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random
__author__ = "Forrest Darling"

#Create empty list to use in show_score function
attempt_list = []

#Funtion to show high score or gives arbitrary message if no high score yet recorded
def show_score():
    if not attempt_list:
        print("You know this other guy got it in like two tries.")
        attempt_list.append(2)
    else:
        print("The current high score is {} attempts".format(min(attempt_list)))


#Main function to run game
def start_game():
    attempts = 0
    range_of = []

    #generate random number for answer to game
    rand_num = random.randint(1, 10)

    #Create list of numbers 1 to 10 to check user input against
    for i in range(1, 11):
        range_of.append(i)
    print("Hello fellow traveler, welcome to the guessing game.")
    user_name = input("What is your name?")

    #Checks if user input is not an empty string if it is prints message to continue game anyways
    if user_name != "":
        print("Nice to meet you {}. Want to play a game? In this game you guess a number between 1 and 10.".format(user_name))
    else:
        print("Alright then keep your secrets. Want to play a game? In this game you guess a number between 1 and 10.")
    ready_play = input("Are you ready to play (yes/no)?")

    #Handles user input to either play game or reprompt until yes/no received
    while True:
        if ready_play == "":
            ready_play = input("Please enter yes/no:")
        elif ready_play.lower() not in ["yes", "no"]:
            ready_play = input("Please enter yes/no:")
        else:
            break

    #exits game if user does not enter yes
    if ready_play.lower() != "yes":
        print("Ok goodbye fellow traveler.")
        exit()

    #Calls show_score function
    show_score()

    #if user inputs yes to ready to play? run this block of code containing the main aspects of the game
    while ready_play.lower() == "yes":
        #Employes try/except to run game code with abilty to handle exceptions
        try:
            guess = int(input("Please enter a number between 1 and 10:"))
            #compares guess to list of numbers 1 to 10 to ensure quality input
            if guess in range_of:
                #If the guess is correct add one to attempts append that to attempt_list and print message to alert user they won
                if guess == rand_num:
                    attempts += 1
                    attempt_list.append(attempts)
                    print("Correct! Great job you guessed right in {} attempts!".format(attempts))
                    play_again = input("Would you like to play again (yes/no)?")
                    #While loop to handle user input on whether they want to play again
                    while True:
                        if play_again == "":
                            play_again = input("Please enter yes/no:")
                        elif play_again.lower() not in ["yes", "no"]:
                            play_again = input("Please enter yes/no:")
                        else:
                            break
                    #If user input is not yes print message and exit game
                    if play_again.lower() != "yes":
                        print("Ok goodbye fellow traveler.")
                        break
                    #If user input is yes reset attempts and pick a new number to restart game
                    else:
                        attempts = 0
                        rand_num = random.randint(1, 10)
                        show_score()
                        continue
                #If the guess is incorrect print message to tell user and allow them to guess again restarting loop
                else:
                    print("Sorry {} is incorrect try again".format(guess))
                    attempts += 1
                    attempt_list.append(attempts)
                    continue
            #If guess is not in range_of or not in 1 to 10 alert user and ask for input in correct range
            else:
                print("{} is not right try again.".format(guess))
                attempt_list.append(attempts)
        #Exception to handle value error or user not inputing a number
        except ValueError:
            print("Please enter a valid number:")
            attempts += 1


#Calls main funciton
if __name__ == "__main__":
    start_game()