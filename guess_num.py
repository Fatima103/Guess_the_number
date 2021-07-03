# 03-07-2021
# In this game the computer choses a random number and the user tries
# to guess it ;)

import random

print("Do you want to play with me")
print("Enter yes if you want to play other wise enter no")
user = str(input()).lower()   #asking the user to play and converting the answer to lower case

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    comperation = guess != random_number 
    while comperation:
        guess = int(input(f"Guess a number between 1 and {x} "))
        # comperation between the user input guess and the random_number
        if guess > random_number:
            print('Sorry, guess a lower number ')
        elif guess < random_number:
            print("Sorry, guess a higher number ")
        elif guess == random_number:
            print("Congrats, you\'re a hero :)")
            #asking the user if he / she wants to play again
            print("Do you want to play again? Enter yes or no... ")
            play_again = str(input()).lower()
            if play_again == "yes":
                new_ramdom_number = random.randint(1, x)
                random_number = new_ramdom_number
                comperation = True
            else:
                print("Thank you, we're always here if you want to play")
                comperation = False
# what is going to happened when the user chose what he / she wants to do
if user == "yes":
    guess(50)
else:
    print("Thank you, we're always here if you want to play")