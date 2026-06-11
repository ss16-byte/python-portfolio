# Day 2 Project
# Date: 6 June 2026
# My first Game
guess = int(input("Guess the number"))
secret = 7

if guess == secret:
    print("You win!!!!!!*sigh*")

while guess != secret:
    print("Try Again*BWAHAHAHAHAHA*")

    guess = int(input("Guess the number"))
    print("You win!")

