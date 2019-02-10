#!/usr/bin/python3
from random import randint

def main():
    # generate a random number
    x = randint(0, 100)

    # get the user input
    inp = input("Guess a number between 100? ")

    # check if user guessed correctly
    if (inp == x):
        print("Well done!! You guessed correctly.")
    else:
        print("Nope!")

if __name__ == "__main__":
    main()