#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random
__author__ = "Forrest Darling"


attempt_list = []


def show_score():
    if not attempt_list:
        print("You know this other guy got it in like two tries.")
    else:
        print("The current high score is {} attempts".format(min(attempt_list)))

def start_game():
    attempts = 0
    range_of = []
    attempt_list.append(2)
    rand_num = random.randint(1, 10)
    for i in range(1, 11):
        range_of.append(i)
    print("Hello fellow traveler, welcome to the guessing game.")
    user_name = input("What is your name?")
    if user_name != "":
        print("Nice to meet you {}. Want to play a game? In this game you guess a number between 1 and 10.".format(user_name))
    else:
        print("Alright then keep your secrets. Want to play a game? In this game you guess a number between 1 and 10.")
    ready_play = input("Are you ready to play (yes/no)?")

    while True:
        if ready_play == "":
            ready_play = input("Please enter yes/no:")
        else:
            break
    if ready_play.lower() != "yes":
        print("Ok goodbye fellow traveler.")
        exit()

    show_score()

    while ready_play.lower() == "yes":

        try:
            guess = int(input("Please enter a number between 1 and 10:"))
            if guess in range_of:
                if guess == rand_num:
                    attempts += 1
                    attempt_list.append(attempts)
                    print("Correct! Great job you guessed right in {} attempts!".format(attempts))
                    play_again = input("Would you like to play again (yes/no)?")
                    while True:
                        if play_again == "":
                            play_again = input("Please enter yes/no:")
                        else:
                            break
                    if play_again.lower() != "yes":
                        print("Ok goodbye fellow traveler.")
                        break
                    else:
                        attempts = 0
                        rand_num = random.randint(1, 10)
                        show_score()
                        continue
                else:
                    print("Sorry {} is incorrect try again".format(guess))
                    attempts += 1
                    attempt_list.append(attempts)
                    continue
            else:
                print("{} is not right try again.".format(guess))
                attempt_list.append(attempts)
        except ValueError:
            print("Please enter a valid number:")
            attempts += 1

if __name__ == "__main__":
    start_game()