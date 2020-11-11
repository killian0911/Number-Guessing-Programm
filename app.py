import random

min = 0
max = 99

number = random.randrange(min, max)

def Guess():

    user_input = input("Pick a number between " + str(min) + " and " + str(max) + " : ")
    
    while user_input != number:
        if str(user_input) < str(number):
            user_input = input("Higher : ")
        elif str(user_input) > str(number):
            user_input = input("Lower : ")
        else:
            print("Congratulations, you guessed the number !")
            break

Guess()
